from typing import List
# from IPython.display import display, Markdown
import asyncio
import time
import os
import shutil
from pathlib import Path
from PIL import Image 

os.environ["CMBAGENT_DEBUG"] = "false"

import cmbagent

from .config import DEFAUL_PROJECT_NAME, INPUT_FILES, PLOTS_FOLDER, DESCRIPTION_FILE, IDEA_FILE, METHOD_FILE, RESULTS_FILE
from .research import Research
from .key_manager import KeyManager
from .llm import LLM, models
from .paper_agents.journal import Journal
from .idea import Idea
from .method import Method
from .experiment import Experiment
from .paper_agents.agents_graph import build_graph
from .utils import llm_parser, input_check
from .langgraph_agents.agents_graph import build_lg_graph


# TODO: unify display and print by new method
class Denario:
    """
    Denario main class. Allows to set the data and tools description, generate a research idea, generate methodology and compute the results. The it can generate the latex draft of a scientific article with a given journal style from the computed results.
    
    It uses two main backends:

    - `cmbagent`,  for detailed planning and control involving numerous agents for the idea, methods and results generation.
    - `langgraph`, for faster idea and method generation, and for the paper writing.

    Args:
        input_data: Input data to be used. Employ default data if `None`.
        project_dir: Directory project. If `None`, create a `project` folder in the current directory.
        clear_project_dir: Clear all files in project directory when initializing if `True`.
    """

    def __init__(self, input_data: Research | None = None,
                 params={}, 
                 project_dir: str | None = None, 
                 clear_project_dir: bool = False):
        
        if project_dir is None:
            project_dir = os.path.join( os.getcwd(), DEFAUL_PROJECT_NAME )
        if not os.path.exists(project_dir):
            os.mkdir(project_dir)

        if input_data is None:
            input_data = Research()  # Initialize with default values
        self.clear_project_dir = clear_project_dir
        self.research = input_data
        self.params = params

        if os.path.exists(project_dir) and clear_project_dir:
            shutil.rmtree(project_dir)
            os.makedirs(project_dir, exist_ok=True)
        self.project_dir = project_dir

        self.plots_folder = os.path.join(self.project_dir, INPUT_FILES, PLOTS_FOLDER)
        # Ensure the folder exists
        os.makedirs(self.plots_folder, exist_ok=True)

        self._setup_input_files()

        # Get keys from environment if they exist
        self.keys = KeyManager()
        self.keys.get_keys_from_env()


    def _setup_input_files(self) -> None:
        input_files_dir = os.path.join(self.project_dir, INPUT_FILES)
        
        # If directory exists, remove it and all its contents
        if os.path.exists(input_files_dir) and self.clear_project_dir:
            shutil.rmtree(input_files_dir)
            
        # Create fresh input_files directory
        os.makedirs(input_files_dir, exist_ok=True)

    def set_data_description(self, data_description: str | None = None) -> None:
        """
        Set the description of the data and tools to be used by the agents.

        Args:
            data_description: String or path to markdown file including the description of the tools and data. If None, assume that a `data_description.md` is present in `project_dir/input_files`.
        """

        if data_description is None:
            try:
                with open(os.path.join(self.project_dir, INPUT_FILES, DESCRIPTION_FILE), 'r') as f:
                    data_description = f.read()
                data_description = data_description.replace("{path_to_project_data}", str(self.project_dir)+ "/project_data/")
            except FileNotFoundError:
                raise FileNotFoundError("Please provide an input string or markdown file with the data description.")

        elif data_description.endswith(".md"):
            with open(data_description, 'r') as f:
                data_description = f.read()

        elif isinstance(data_description, str):
            pass

        else:
            raise ValueError("Data description must be a string, a path to a markdown file or None if you want to load data description from input_files/data_description.md")

        self.research.data_description = data_description

        # overwrite the data_description.md file
        with open(os.path.join(self.project_dir, INPUT_FILES, DESCRIPTION_FILE), 'w') as f:
            f.write(data_description)

    def show_data_description(self) -> None:
        """Show the data description set by the `set_data_description` method."""

        # display(Markdown(self.research.data_description))
        print(self.research.data_description)

    # TODO: some code duplication with set_idea, get_idea could call set_idea internally after generating ideas
    def get_idea(self,
                 idea_maker_model: LLM | str = models["gpt-4o"],
                 idea_hater_model: LLM | str = models["claude-3.7-sonnet"],
                ) -> None:
        """Generate an idea making use of the data and tools described in `data_description.md`.
        Args:
           idea_maker_model: the LLM to be used for the idea maker agent. Default is gpt-4o.
           idea_hater_model: the LLM to be used for the idea hater agent. Default is claude-3.7-sonnet
        """

        # Get LLM instances
        idea_maker_model = llm_parser(idea_maker_model)
        idea_hater_model = llm_parser(idea_hater_model)
        
        if self.research.data_description == "":
            with open(os.path.join(self.project_dir, INPUT_FILES, DESCRIPTION_FILE), 'r') as f:
                self.research.data_description = f.read()

        idea = Idea(work_dir = self.project_dir,
                    idea_maker_model = idea_maker_model.name,
                    idea_hater_model = idea_hater_model.name,
                    keys=self.keys)
        
        idea = idea.develop_idea(self.research.data_description)
        self.research.idea = idea
        # Write idea to file
        idea_path = os.path.join(self.project_dir, INPUT_FILES, IDEA_FILE)
        with open(idea_path, 'w') as f:
            f.write(idea)

        self.idea = idea

    def get_idea_fast(self, llm: LLM | str = models["gemini-2.0-flash"],
                      verbose=False) -> None:
        """
        Generate an idea using the idea maker - idea hater method.
        
        Args:
           - llm: the LLM model to be used
           - verbose: whether to stream the LLM response
        """

        # Start timer
        start_time = time.time()
        config = {"configurable": {"thread_id": "1"}, "recursion_limit":100}

        # Get LLM instance
        llm = llm_parser(llm)

        # Build graph
        graph = build_lg_graph(mermaid_diagram=False)

        # get name of data description file
        f_data_description = os.path.join(self.project_dir, INPUT_FILES, DESCRIPTION_FILE)

        # Initialize the state
        input_state = {
            "task": "idea_generation",
            "files":{"Folder": self.project_dir,
                     "data_description": f_data_description}, #name of project folder
            "llm": {"model": llm.name,                #name of the LLM model to use
                    "temperature": llm.temperature,
                    "max_output_tokens": llm.max_output_tokens,
                    "stream_verbose": verbose},
            "keys": self.keys,
            "idea": {"total_iterations": 4},
        }
        
        # Run the graph
        graph.invoke(input_state, config)
        
        # End timer and report duration in minutes and seconds
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"Idea generated in {minutes} min {seconds} sec.")  
        
    def set_idea(self, idea: str = None) -> None:
        """Manually set an idea, either directly from a string or providing the path of a markdown file with the idea."""

        if idea is None:
            with open(os.path.join(self.project_dir, INPUT_FILES, IDEA_FILE), 'r') as f:
                idea = f.read()

        idea = input_check(idea)
        
        self.research.idea = idea
        
        with open(os.path.join(self.project_dir, INPUT_FILES, IDEA_FILE), 'w') as f:
            f.write(idea)

        self.research.idea = idea
    
    def show_idea(self) -> None:
        """Show the provided or generated idea by the `set_idea` or `get_idea` methods."""

        # display(Markdown(self.research.idea))
        print(self.research.idea)

    def check_idea(self) -> str:
        """use futurehouse to check the idea against previous literature"""
        from futurehouse_client import FutureHouseClient, JobNames
        from futurehouse_client.models import (
            TaskRequest,
        )
        import os
        fhkey = os.getenv("FUTURE_HOUSE_API_KEY")


        fh_client = FutureHouseClient(
            api_key=fhkey,
        )

        check_idea_prompt = rf"""
        Has anyone worked on or explored the following idea?

        {self.research.idea}
        
        <DESIRED_RESPONSE_FORMAT>
        Answer: <yes or no>

        Related previous work: <describe previous literature on the topic>
        </DESIRED_RESPONSE_FORMAT>
        """
        task_data = TaskRequest(name=JobNames.from_string("owl"),
                                query=check_idea_prompt)
        
        task_response = fh_client.run_tasks_until_done(task_data)

        return task_response[0].formatted_answer


    
    def get_method(self) -> None:
        """Generate the methods to be employed making use of the data and tools described in `data_description.md` and the idea in `idea.md`."""

        if self.research.data_description == "":
            with open(os.path.join(self.project_dir, INPUT_FILES, DESCRIPTION_FILE), 'r') as f:
                self.research.data_description = f.read()        

        if self.research.idea == "":
            with open(os.path.join(self.project_dir, INPUT_FILES, IDEA_FILE), 'r') as f:
                self.research.idea = f.read()

        method = Method(self.research.idea, keys=self.keys,  work_dir = self.project_dir)
        methododology = method.develop_method(self.research.data_description)
        self.research.methodology = methododology

        # Write idea to file
        method_path = os.path.join(self.project_dir, INPUT_FILES, METHOD_FILE)
        with open(method_path, 'w') as f:
            f.write(methododology)

    def get_method_fast(self, llm: LLM | str = models["gemini-2.0-flash"],
                        verbose=False) -> None:
        """Generate the methods to be employed making use of the data and tools described in `data_description.md` and the idea in `idea.md`. Faster version get_method.
        Args:
           - llm: the LLM model to be used
           - verbose: whether to stream the LLM response
        """

        # Start timer
        start_time = time.time()
        config = {"configurable": {"thread_id": "1"}, "recursion_limit":100}

        # Get LLM instance
        llm = llm_parser(llm)

        # Build graph
        graph = build_lg_graph(mermaid_diagram=False)

        # get name of data description file and idea
        f_data_description = os.path.join(self.project_dir, INPUT_FILES, DESCRIPTION_FILE)
        f_idea = os.path.join(self.project_dir, INPUT_FILES, IDEA_FILE)
        
        # Initialize the state
        input_state = {
            "task": "methods_generation",
            "files":{"Folder": self.project_dir,              #name of project folder
                     "data_description": f_data_description,
                     "idea": f_idea}, 
            "llm": {"model": llm.name,                #name of the LLM model to use
                    "temperature": llm.temperature,
                    "max_output_tokens": llm.max_output_tokens,
                    "stream_verbose": verbose},
            "keys": self.keys,
            "idea": {"total_iterations": 4},
        }
        
        # Run the graph
        graph.invoke(input_state, config)
        
        # End timer and report duration in minutes and seconds
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"Methods generated in {minutes} min {seconds} sec.")  
        
    def set_method(self, method: str = None) -> None:
        """Manually set methods, either directly from a string or providing the path of a markdown file with the methods."""

        method = input_check(method)
        
        self.research.methodology = method
        
        with open(os.path.join(self.project_dir, INPUT_FILES, METHOD_FILE), 'w') as f:
            f.write(method)
    
    def show_method(self) -> None:
        """Show the provided or generated methods by `set_method` or `get_method`."""

        # display(Markdown(self.research.methodology))
        print(self.research.methodology)

    def get_results(self,
                    involved_agents: List[str] = ['engineer', 'researcher'],
                    engineer_model: LLM | str = models["claude-3.7-sonnet"],
                    researcher_model: LLM | str = models["o3-mini"],
                    restart_at_step: int = -1
                    ) -> None:
        """
        Compute the results making use of the methods, idea and data description.

        Args:
            involved_agents: List of agents employed to compute the results.
        """

        # Get LLM instances
        engineer_model = llm_parser(engineer_model)
        researcher_model = llm_parser(researcher_model)

        if self.research.data_description == "":
            with open(os.path.join(self.project_dir, INPUT_FILES, DESCRIPTION_FILE), 'r') as f:
                self.research.data_description = f.read()

        if self.research.idea == "":
            with open(os.path.join(self.project_dir, INPUT_FILES, IDEA_FILE), 'r') as f:
                self.research.idea = f.read()

        if self.research.methodology == "":
            with open(os.path.join(self.project_dir, INPUT_FILES, METHOD_FILE), 'r') as f:
                self.research.methodology = f.read()

        experiment = Experiment(research_idea=self.research.idea,
                                methodology=self.research.methodology,
                                involved_agents=involved_agents,
                                engineer_model=engineer_model.name,
                                researcher_model=researcher_model.name,
                                work_dir = self.project_dir,
                                keys=self.keys,
                                restart_at_step = restart_at_step)
        experiment.run_experiment(self.research.data_description)
        self.research.results = experiment.results
        self.research.plot_paths = experiment.plot_paths

        # move plots to the plots folder in input_files/plots 
        ## Clearing the folder
        if os.path.exists(self.plots_folder):
            for file in os.listdir(self.plots_folder):
                file_path = os.path.join(self.plots_folder, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
        for plot_path in self.research.plot_paths:
            shutil.move(plot_path, self.plots_folder)

        # Write results to file
        results_path = os.path.join(self.project_dir, INPUT_FILES, RESULTS_FILE)
        with open(results_path, 'w') as f:
            f.write(self.research.results)

    def set_results(self, results: str = None) -> None:
        """Manually set the results, either directly from a string or providing the path of a markdown file with the results."""

        results = input_check(results)
        
        self.research.results = results
        
        with open(os.path.join(self.project_dir, INPUT_FILES, RESULTS_FILE), 'w') as f:
            f.write(results)

    def set_plots(self, plots: list[str] | list[Image.Image]) -> None:
        """Manually set the plots from their path."""

        for i, plot in enumerate(plots):
            if isinstance(plot,str):
                plot_path= Path(plot)
                img = Image.open(plot_path)
                plot_name = str(plot_path.name)
            else:
                img = plot
                plot_name = f"plot_{i}.png"
            
            img.save( os.path.join(self.project_dir, INPUT_FILES, PLOTS_FOLDER, plot_name) )
    
    def show_results(self) -> None:
        """Show the obtained results."""

        # display(Markdown(self.research.results))
        print(self.research.results)
    
    def get_keywords(self, input_text: str, n_keywords: int = 5) -> None:
        """
        Get AAS keywords from input text using cmbagent.

        Args:
            input_text (str): Text to extract keywords from
            n_keywords (int, optional): Number of keywords to extract. Defaults to 5.

        Returns:
            dict: Dictionary mapping AAS keywords to their URLs
        """
        
        aas_keywords = cmbagent.get_keywords(input_text, n_keywords = n_keywords, api_keys = self.keys)
        self.research.keywords = aas_keywords
    
    def show_keywords(self) -> None:
        """Show the AAS keywords."""

        AAS_keyword_list = "\n".join(
                            [f"- [{keyword}]({self.research.keywords[keyword]})" for keyword in self.research.keywords]
                        )
        # display(Markdown(AAS_keyword_list))
        print(AAS_keyword_list)

    def get_paper(self,
                  journal: Journal = Journal.NONE,
                  llm: LLM | str = models["gemini-2.5-flash"],
                  writer: str = 'scientist',
                  cmbagent_keywords: bool = False,
                  add_citations=True) -> None:
        """
        Generate a full paper based on the files in input_files:

            - idea.md
            - methods.md
            - results.md
            - plots

        Different journals considered

            - NONE = None : No journal, use standard latex presets with unsrt for bibliography style.
            - AAS  = "AAS" : American Astronomical Society journals, including the Astrophysical Journal.
            - APS = "APS" : Physical Review Journals from the American Physical Society, including Physical Review Letters, PRA, etc.
            - ICML = "ICML" : ICML - International Conference on Machine Learning.
            - JHEP = "JHEP" : Journal of High Energy Physics, including JHEP, JCAP, etc.
            - NeurIPS = "NeurIPS" : NeurIPS - Conference on Neural Information Processing Systems.
            - PASJ = "PASJ" : Publications of the Astronomical Society of Japan.

        Args:
            journal: Journal style. The paper generation will use the presets of the journal considered for the latex writing. Default is no journal (no specific presets).
            llm: The LLM model to be used to write the paper. Default is set to gemini-2.0-flash
            writer: set the style and tone to write. E.g. astrophysicist, biologist, chemist
            cmbagent_keywords: whether to use CMBAgent to select the keywords
            add_citations: whether to add citations to the paper or not
        """
        
        # Start timer
        start_time = time.time()
        config = {"configurable": {"thread_id": "1"}, "recursion_limit":100}

        # Get LLM instance
        llm = llm_parser(llm)

        # Build graph
        graph = build_graph(mermaid_diagram=False)

        # Initialize the state
        input_state = {
            "files":{"Folder": self.project_dir}, #name of project folder
            "llm": {"model": llm.name,  #name of the LLM model to use
                    "temperature": llm.temperature,
                    "max_output_tokens": llm.max_output_tokens},
            "paper":{"journal": journal, "add_citations": add_citations,
                     "cmbagent_keywords": cmbagent_keywords},
            "keys": self.keys,
            "writer": writer,
        }

        # Run the graph
        asyncio.run(graph.ainvoke(input_state, config))
        
        # End timer and report duration in minutes and seconds
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"Paper written in {minutes} min {seconds} sec.")    

    def research_pilot(self, data_description: str = None) -> None:
        """Full run of Denario. It calls the following methods sequentially:
        ```
        set_data_description(data_description)
        get_idea()
        get_method()
        get_results()
        get_paper()
        ```
        """

        self.set_data_description(data_description)
        self.get_idea()
        self.get_method()
        self.get_results()
        self.get_paper()

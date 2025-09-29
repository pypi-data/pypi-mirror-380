import os
from langchain_core.runnables import RunnableConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from .parameters import GraphState
from ..config import INPUT_FILES, IDEA_FILE, METHOD_FILE

def preprocess_node(state: GraphState, config: RunnableConfig):
    """
    This agent reads the input files, clean up files, and set the name of some files
    """
    
    # set the LLM
    if 'gemini' in state['llm']['model']:
        state['llm']['llm'] = ChatGoogleGenerativeAI(model=state['llm']['model'],
                                                temperature=state['llm']['temperature'],
                                                google_api_key=state["keys"].GEMINI)

    elif any(key in state['llm']['model'] for key in ['gpt', 'o3']):
        state['llm']['llm'] = ChatOpenAI(model=state['llm']['model'],
                                         temperature=state['llm']['temperature'],
                                         openai_api_key=state["keys"].OPENAI)
                    
    elif 'claude' in state['llm']['model']  or 'anthropic' in state['llm']['model'] :
        state['llm']['llm'] = ChatAnthropic(model=state['llm']['model'],
                                            temperature=state['llm']['temperature'],
                                            anthropic_api_key=state["keys"].ANTHROPIC)
    
    # set the tokens usage
    state['tokens'] = {'ti': 0, 'to': 0, 'i': 0, 'o': 0}

    # read data description
    try:
        with open(state['files']['data_description'], 'r', encoding='utf-8') as f:
            description = f.read()
    except FileNotFoundError:
        raise Exception("Data description file not found!")
    except Exception:
        raise Exception("Error reading the data description file!")

    # read idea description
    if state['task']=='methods_generation':
        try:
            with open(state['files']['idea'], 'r', encoding='utf-8') as f:
                idea = f.read()
        except FileNotFoundError:
            raise Exception("Data description file not found!")
        except Exception:
            raise Exception("Error reading the data description file!")
    
    # set the name of the common files
    if state['task']=='idea_generation':
        state['files']['module_folder'] = 'idea_generation_output'
        state['files']['f_stream'] = f"{state['files']['Folder']}/{state['files']['module_folder']}/idea.log"
    elif state['task']=='methods_generation':
        state['files']['module_folder'] = 'methods_generation_output'
        state['files']['f_stream'] = f"{state['files']['Folder']}/{state['files']['module_folder']}/methods.log"
    state['files'] = {**state['files'],
                      "Temp":      f"{state['files']['Folder']}/{state['files']['module_folder']}",
                      "LLM_calls": f"{state['files']['Folder']}/{state['files']['module_folder']}/LLM_calls.txt",
                      "Error":     f"{state['files']['Folder']}/{state['files']['module_folder']}/Error.txt",
    }

    # set particulars for different tasks
    if state['task']=='idea_generation':
        idea = {**state['idea'], 'iteration':0, 'previous_ideas': "",
                'idea': "", 'criticism': ""}
        state['files'] = {**state['files'],
                          "idea":      f"{state['files']['Folder']}/{INPUT_FILES}/{IDEA_FILE}",
                          "idea_log":  f"{state['files']['Folder']}/{state['files']['module_folder']}/idea.log",
        }
    elif state['task']=='methods_generation':
        state['files'] = {**state['files'],
                          "methods": f"{state['files']['Folder']}/{INPUT_FILES}/{METHOD_FILE}",
        }
        idea = {**state['idea'], 'idea': idea}
        

    # create project folder, input files, and temp files
    os.makedirs(state['files']['Folder'],                    exist_ok=True)
    os.makedirs(state['files']['Temp'],                      exist_ok=True)
    os.makedirs(f"{state['files']['Folder']}/{INPUT_FILES}", exist_ok=True)
    os.makedirs(f"{state['files']['module_folder']}",        exist_ok=True)

    # clean existing files
    for f in ["LLM_calls", "Error"]:
        file_path = state['files'][f]
        if os.path.exists(file_path):
            os.remove(file_path)

    if state['task']=='idea_generation':
        for f in ["idea", "idea_log"]:
            file_path = state['files'][f]
            if os.path.exists(file_path):
                os.remove(file_path)
                
    if state['task']=='methods_generation':
        for f in ["methods"]:
            file_path = state['files'][f]
            if os.path.exists(file_path):
                os.remove(file_path)

    return {**state,
            "files":            state['files'],
            "llm":              state['llm'],
            "tokens":           state['tokens'],
            "data_description": description,
            "idea":             idea}


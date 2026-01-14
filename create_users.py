
import json
import random
import nltk
nltk.download("words")
from nltk.corpus import words
import secrets
import pandas as pd

SYMBOLS = list(range(20))
SYMBOLS.extend(["?", "!", ".", ","])
TASKS = ["Argumentative Writing", "Creative Writing", "Explanatory Writing"]
NO_LLM_TASKS = ["Argumentative Writing", "Creative Writing", "Explanatory Writing"]
LLMS = ['deepseek-chat', 'gpt-5.2', 'gemini-3-flash-preview', 'qwen2.5:7b', 'llama4:scout']
TEMPERATURES = [0, 1]

def randomize(arr: list[str]) -> list[str]:
    """
    Random shuffling of the list.
    
    :param arr: list of available LLMs
    :type arr: list[str]
    :return: shuffled list of available LLMs
    :rtype: list[str]
    """
    return random.sample(arr, len(arr))

def assign_llms_to_tasks(sorted_llms: list[str], sorted_temperatures: list[float], n_tasks: int) -> dict[int, str | float]:
    """
    Assigns an LLM and a temperature to each task.
    
    :param sorted_llms: available models
    :type sorted_llms: list[str]
    :param sorted_temperatures: possible temperatures
    :type sorted_temperatures: list[float]
    :param n_tasks: A dictionary in form {taskId: {model: modelName, temperature: temperatureValue}, ..}
    :type n_tasks: int
    """
    task_llm_assignment = {}
    randomized_tasks = randomize(TASKS)
    for i in range(n_tasks):
        if not sorted_llms:
            sorted_llms.extend(randomize(LLMS))
        if not sorted_temperatures:
            sorted_temperatures.extend(randomize(TEMPERATURES))
        if i > 0:
            task_llm_assignment[i] = {"model": sorted_llms.pop(),
                                      "temperature": sorted_temperatures.pop(),
                                      "task": randomized_tasks.pop()}
        else:
            task_llm_assignment[i] = {"model": sorted_llms.pop(),
                                      "temperature": sorted_temperatures.pop(),
                                      "task": "Warm-up"}

    return task_llm_assignment

def create_users(n: int, n_tasks: int = 4):
    """
    Creates a list of n users and assigns LLMs to them
    
    :param n: number of users
    :type n: int
    :param n_tasks: number of tasks for each user
    :type n_tasks: int
    """
    users = []
    usernames = random.sample(words.words(), n)
    sorted_llms = randomize(LLMS)
    sorted_temperatures = randomize(TEMPERATURES)
    sorted_no_llms = randomize(NO_LLM_TASKS)

    for i, username in enumerate(usernames):
        username = username.lower()
        password = ""
        for _ in range(2):
            password += str.capitalize(secrets.choice(words.words()))
            password += str(secrets.choice(SYMBOLS))
        ext_id = random.randint(100, 1000)
        task_llm_assignment = assign_llms_to_tasks(sorted_llms, sorted_temperatures, n_tasks)
        if not sorted_no_llms:
            sorted_no_llms.extend(randomize(NO_LLM_TASKS))
        no_llm_task = sorted_no_llms.pop()
        user = {
            "extId": ext_id,
            "firstName": "user",
            "lastName": "user",
            "userName": username,
            "email": username + "@email.com",
            "roles": "Student*in",
            "password": password,
            "modelTaskMapping": {"noLLM": no_llm_task, "LLM": task_llm_assignment}
        }
        users.append(user)
    return users

def save_as_csv(users: list[list], path: str) -> None:
    """
    Save user data as csv
    
    :param users: List of user data
    :type users: list[list]
    :param path: Path to csv file
    :type path: str
    """
    df = pd.DataFrame(data=users)
    df["modelTaskMapping"] = df["modelTaskMapping"].apply(json.dumps)
    df.to_csv(path, index=False)

def main():
    n_users = 3
    n_tasks = 4
    path = "users/users.csv"
    users = create_users(n_users, n_tasks)
    save_as_csv(users, path)

if __name__ == "__main__":
    main()
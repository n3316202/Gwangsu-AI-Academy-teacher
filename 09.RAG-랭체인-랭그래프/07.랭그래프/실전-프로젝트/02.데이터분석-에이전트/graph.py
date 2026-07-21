from langgraph.graph import StateGraph
from langgraph.graph import START, END

from langchain.chat_models import init_chat_model
from state import AnalysisState
from tools import *


# ----------------------
# LLM
# ----------------------
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent.parent.parent)
)

from llm_loader import init_custom_llm

llm = init_custom_llm()

# ----------------------
# CSV
# ----------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "sales.csv"

df = load_csv(str(DATA_PATH))
print(df)
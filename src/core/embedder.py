#!/usr/bin/env python3

from langchain.vectorstores import DeepLake
from langchain.embeddings.openai import OpenAIEmbeddings
from ..config import Config

embeddings = OpenAIEmbeddings()

class CodeEmbedder:
    def __init__(self, code_chunks):
        self.code_chunks = code_chunks
        self.username = Config.activeloop_username
        self.embeddings = []

    def embed_code(self):
        """
        Embed the code chunks using a pre-trained SentenceTransformer model.
        """
        db = DeepLake.from_documents(texts, embeddings, dataset_path=f"hub://{self.username}/langchain-code")
        self.embeddings = self.model.encode(self.code_chunks)

    def get_embeddings(self):
        """
        Return the list of embeddings.
        """
        return self.embeddings
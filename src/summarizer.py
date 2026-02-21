from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class YouTubeSummarizer:
    def __init__(self, model_name: str = "openai/gpt-oss-20b"):
        self.client = Groq(api_key=os.getenv("groq_api_key"))
        self.model = model_name

        # Character-based splitting (safe + stable)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=4000,
            chunk_overlap=300
        )

    def build_prompt(self, text: str, summary_type: str) -> str:
        """
        Builds dynamic prompt based on selected summary type.
        """

        summary_type = summary_type.lower()

        if summary_type == "concise":
            instruction = "Provide a concise and clear summary of the content."

        elif summary_type == "bullet":
            instruction = "Summarize the content in structured bullet points highlighting key ideas."

        elif summary_type == "insights":
            instruction = "Extract only the most important insights and actionable takeaways."

        elif summary_type == "detailed":
            instruction = "Provide a detailed explanation covering all major concepts discussed."

        elif summary_type == "blog":
            instruction = (
                "Rewrite this as an engaging blog-style article with smooth flow, "
                "clear sections, and reader-friendly tone."
            )

        elif summary_type == "twitter":
            instruction = (
                "Convert this into a Twitter thread with short, impactful posts. "
                "Number each tweet clearly."
            )

        else:
            instruction = "Provide a clear and structured summary."

        return f"""
            You are an expert content summarizer.
            {instruction}
            Transcript:
            {text}
            """
    
    def split_text(self, text: str):
        """
        Splits transcript into manageable overlapping chunks.
        """
        return self.text_splitter.split_text(text)

    def summarize_chunk(self, chunk: str, summary_type: str) -> str:
        """
        Summarizes a single chunk of transcript.
        """

        prompt = self.build_prompt(chunk, summary_type)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert content summarizer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    def refine_summary(self, combined_text: str, summary_type: str) -> str:
        """
        Refines combined chunk summaries into final structured output.
        """

        refinement_prompt = f"""
            You are an expert content editor.

            Refine and merge the following partial summaries into one final, well-structured output.
            Remove repetition and improve clarity.

            Maintain the requested format: {summary_type}

            Content:
            {combined_text}
            """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert content editor."},
                {"role": "user", "content": refinement_prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    def generate_summary(self, transcript: str, summary_type: str = "concise") -> str:
        """
        Executes full hierarchical Map-Reduce summarization.
        """

        chunks = self.split_text(transcript)

        partial_summaries = []

        for chunk in chunks:
            summary = self.summarize_chunk(chunk, summary_type)
            partial_summaries.append(summary)

        combined_summary = "\n\n".join(partial_summaries)

        final_summary = self.refine_summary(combined_summary, summary_type)

        return final_summary

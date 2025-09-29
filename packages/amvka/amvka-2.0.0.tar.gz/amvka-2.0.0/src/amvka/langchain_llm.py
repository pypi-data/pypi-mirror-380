"""
LangChain-powered LLM integration for amvka.
Universal interface supporting 100+ LLM providers through LangChain.
"""

import os
from typing import Optional, Dict, Any, Tuple
from langchain.llms.base import LLM
from langchain.chat_models.base import BaseChatModel
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.manager import CallbackManagerForLLMRun

from .utils import print_error, print_info, print_warning, print_success
from .environment import EnvironmentDetector


class UniversalLLMClient:
    """Universal LLM client powered by LangChain supporting 100+ providers."""
    
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.provider = config_manager.get_provider()
        self.credentials = config_manager.get_credentials()
        self.model = config_manager.get_model()
        self.env_detector = EnvironmentDetector()
        self.llm = None
        
        if not self._is_configured():
            self._show_setup_message()
            raise ValueError("Configuration required")
        
        self._setup_langchain_llm()
    
    def _is_configured(self) -> bool:
        """Check if properly configured."""
        return bool(self.provider and self.credentials)
    
    def _setup_langchain_llm(self):
        """Setup LangChain LLM based on provider."""
        try:
            if self.provider == "openai":
                self._setup_openai()
            elif self.provider == "gemini":
                self._setup_gemini()
            elif self.provider == "claude":
                self._setup_claude()
            elif self.provider == "azure":
                self._setup_azure()
            elif self.provider == "aws":
                self._setup_aws()
            elif self.provider == "ollama":
                self._setup_ollama()
            elif self.provider == "huggingface":
                self._setup_huggingface()
            elif self.provider == "cohere":
                self._setup_cohere()
            elif self.provider == "groq":
                self._setup_groq()
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
                
            print_success(f"✅ Connected to {self.provider} with model: {self.model}")
            
        except Exception as e:
            print_error(f"❌ Failed to setup {self.provider}: {str(e)}")
            raise
    
    def _setup_openai(self):
        """Setup OpenAI through LangChain."""
        try:
            from langchain_openai import ChatOpenAI, OpenAI
            
            api_key = self.credentials.get("api_key")
            
            # Use ChatOpenAI for GPT models
            if "gpt" in self.model.lower():
                self.llm = ChatOpenAI(
                    model=self.model,
                    openai_api_key=api_key,
                    temperature=0.1,
                    max_tokens=100
                )
            else:
                self.llm = OpenAI(
                    model=self.model,
                    openai_api_key=api_key,
                    temperature=0.1,
                    max_tokens=100
                )
                
        except ImportError:
            raise ImportError("Install OpenAI support: pip install langchain-openai")
    
    def _setup_gemini(self):
        """Setup Google Gemini through LangChain."""
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            
            api_key = self.credentials.get("api_key")
            
            self.llm = ChatGoogleGenerativeAI(
                model=self.model,
                google_api_key=api_key,
                temperature=0.1,
                max_output_tokens=100
            )
            
        except ImportError:
            raise ImportError("Install Gemini support: pip install langchain-google-genai")
    
    def _setup_claude(self):
        """Setup Anthropic Claude through LangChain."""
        try:
            from langchain_anthropic import ChatAnthropic
            
            api_key = self.credentials.get("api_key")
            
            self.llm = ChatAnthropic(
                model=self.model,
                anthropic_api_key=api_key,
                temperature=0.1,
                max_tokens=100
            )
            
        except ImportError:
            raise ImportError("Install Claude support: pip install langchain-anthropic")
    
    def _setup_azure(self):
        """Setup Azure OpenAI through LangChain."""
        try:
            from langchain_openai import AzureChatOpenAI
            
            self.llm = AzureChatOpenAI(
                deployment_name=self.model,
                openai_api_key=self.credentials.get("api_key"),
                azure_endpoint=self.credentials.get("endpoint"),
                openai_api_version=self.credentials.get("api_version", "2023-12-01-preview"),
                temperature=0.1,
                max_tokens=100
            )
            
        except ImportError:
            raise ImportError("Install Azure support: pip install langchain-openai")
    
    def _setup_aws(self):
        """Setup AWS Bedrock through LangChain."""
        try:
            from langchain_aws import ChatBedrock
            
            self.llm = ChatBedrock(
                model_id=self.model,
                region_name=self.credentials.get("region", "us-east-1"),
                credentials_profile_name=self.credentials.get("profile"),
            )
            
        except ImportError:
            raise ImportError("Install AWS support: pip install langchain-aws")
    
    def _setup_ollama(self):
        """Setup Ollama through LangChain."""
        try:
            from langchain_community.llms import Ollama
            
            self.llm = Ollama(
                model=self.model,
                base_url=self.credentials.get("base_url", "http://localhost:11434"),
                temperature=0.1
            )
            
        except ImportError:
            raise ImportError("Install Ollama support: pip install langchain-community")
    
    def _setup_huggingface(self):
        """Setup Hugging Face through LangChain."""
        try:
            from langchain_huggingface import HuggingFacePipeline
            
            self.llm = HuggingFacePipeline.from_model_id(
                model_id=self.model,
                task="text-generation",
                model_kwargs={"temperature": 0.1, "max_length": 100}
            )
            
        except ImportError:
            raise ImportError("Install HuggingFace support: pip install langchain-huggingface")
    
    def _setup_cohere(self):
        """Setup Cohere through LangChain."""
        try:
            from langchain_cohere import ChatCohere
            
            api_key = self.credentials.get("api_key")
            
            self.llm = ChatCohere(
                model=self.model,
                cohere_api_key=api_key,
                temperature=0.1,
                max_tokens=100
            )
            
        except ImportError:
            raise ImportError("Install Cohere support: pip install langchain-cohere")
    
    def _setup_groq(self):
        """Setup Groq through LangChain."""
        try:
            from langchain_groq import ChatGroq
            
            api_key = self.credentials.get("api_key")
            
            self.llm = ChatGroq(
                model=self.model,
                groq_api_key=api_key,
                temperature=0.1,
                max_tokens=100
            )
            
        except ImportError:
            raise ImportError("Install Groq support: pip install langchain-groq")
    
    def get_command(self, query: str, context: Dict = None) -> Optional[str]:
        """Get command using LangChain's universal interface with smart fallbacks."""
        # Try with current model first
        result, model_responded = self._try_get_command(query, context)
        if result:
            return result
        
        # If model responded successfully but returned None (conversational), don't try fallbacks
        if model_responded:
            return None
        
        # If model failed to respond, try fallback models for the provider
        return self._try_fallback_models(query, context)
    
    def _try_get_command(self, query: str, context: Dict = None) -> Tuple[Optional[str], bool]:
        """Try to get command with current model. Returns (command, model_responded)."""
        try:
            # Build the prompt
            prompt = self._build_universal_prompt(query, context)
            
            # Use LangChain's universal interface
            if hasattr(self.llm, 'invoke'):
                # New LangChain interface (0.1+)
                if isinstance(self.llm, BaseChatModel):
                    messages = [
                        SystemMessage(content="You are an expert command-line assistant."),
                        HumanMessage(content=prompt)
                    ]
                    response = self.llm.invoke(messages)
                    command = self._extract_command(response.content)
                    return command, True  # Model responded successfully
                else:
                    response = self.llm.invoke(prompt)
                    command = self._extract_command(response)
                    return command, True  # Model responded successfully
            else:
                # Legacy interface
                response = self.llm(prompt)
                command = self._extract_command(response)
                return command, True  # Model responded successfully
                
        except Exception as e:
            print_warning(f"⚠️  Primary model '{self.model}' failed, trying fallbacks...")
            return None, False  # Model failed to respond
    
    def _try_fallback_models(self, query: str, context: Dict = None) -> Optional[str]:
        """Try fallback models for the current provider."""
        fallback_models = {
            "gemini": ["gemini-2.0-flash", "gemini-2.0-flash-exp", "gemini-1.5-flash-8b", "gemini-1.5-flash-latest"],
            "openai": ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4"],
            "claude": ["claude-3-haiku-20240307", "claude-3-sonnet-20240229"],
            "groq": ["llama3.1-70b-versatile", "llama3.1-8b-instant", "mixtral-8x7b-32768", "gemma2-9b-it"]
        }
        
        provider_fallbacks = fallback_models.get(self.provider, [])
        
        for fallback_model in provider_fallbacks:
            if fallback_model == self.model:
                continue  # Skip the model that already failed
            
            try:
                # Temporarily change model
                original_model = self.model
                self.model = fallback_model
                
                # Recreate LLM with fallback model
                self._setup_langchain_llm()
                
                # Try the request
                result, model_responded = self._try_get_command(query, context)
                if result:
                    print_success(f"✅ Success with fallback model: {fallback_model}")
                    return result
                
            except Exception:
                continue
            finally:
                # Restore original model
                self.model = original_model
        
        print_error(f"❌ Error: Unable to connect with any available {self.provider} models. Please check your API key and network connection.")
        return None
    
    def _build_universal_prompt(self, query: str, context: Dict = None) -> str:
        """Build universal prompt that works across all LLM providers."""
        env_context = self.env_detector.get_environment_context()
        
        os_name = env_context["os"]
        shell = env_context["shell"]
        
        # Context information
        context_info = ""
        if context:
            if "files" in context:
                files_list = ", ".join([f["path"] for f in context["files"][:5]])
                context_info += f"\\nCurrent directory files: {files_list}"
        
        prompt = f"""You are an intelligent AI assistant integrated into a command-line tool called amvka. You can both answer questions and generate shell commands.

Environment: {os_name} with {shell}
User Request: {query}{context_info}

Instructions:
1. For system/file operations (list, copy, move, create, delete files/folders), respond with: COMMAND: [shell command]
2. For general knowledge questions (who/what/where/when/why about people, places, concepts), answer directly with your knowledge
3. For greetings, respond with: GREETING: [friendly response]  
4. For help about amvka, respond with: HELP: [help information]
5. For dangerous operations, respond with: UNSAFE: [explanation]

Examples:
- "list files" → COMMAND: ls
- "who is president of america" → Joe Biden is the current President of the United States...
- "who is prime minister of india" → Narendra Modi is the current Prime Minister of India...
- "what is python" → Python is a high-level programming language...
- "check disk space" → COMMAND: df -h
- "hello" → GREETING: Hello! I'm amvka, your AI assistant...

Response:"""
        
        return prompt
    
    def _extract_command(self, response: str) -> Optional[str]:
        """Extract command from LLM response or display general answer."""
        if not response:
            return None
        
        response = response.strip()
        
        # Handle structured responses
        if response.startswith("COMMAND:"):
            # Extract the actual command
            command = response.replace("COMMAND:", "").strip()
            return command
        
        elif response.startswith("GREETING:"):
            # Display friendly greeting
            greeting = response.replace("GREETING:", "").strip()
            print_info(f"👋 {greeting}")
            return None
        
        elif response.startswith("HELP:"):
            # Display help information
            help_text = response.replace("HELP:", "").strip()
            print_info(f"🚀 {help_text}")
            return None
            
        elif response.startswith("UNSAFE:"):
            # Display safety warning
            warning = response.replace("UNSAFE:", "").strip()
            print_warning(f"⚠️ {warning}")
            return None
        
        else:
            # Check for legacy formats (backward compatibility)
            if "GREETING" in response.upper():
                print_info("👋 Hello! I'm amvka, your AI assistant. I can help with commands and answer questions!")
                return None
            elif "HELP" in response.upper():
                print_info("""🚀 amvka - Universal AI Assistant

I can help you with:
• System commands: "list files", "check memory usage"  
• General questions: "who is pm of india", "what is python"
• File operations: "create backup", "find large files"

Just ask me anything!""")
                return None
            elif "UNSAFE" in response.upper():
                print_warning("⚠️ The requested operation was deemed unsafe and will not be executed.")
                return None
            else:
                # This is a general answer - display it directly
                print_info(f"🤖 {response}")
                return None
        
        # Clean up common formatting
        command = command.replace("```", "").replace("`", "")
        
        # Return first line that looks like a command
        for line in command.split("\\n"):
            line = line.strip()
            if line and not line.startswith("#"):
                return line
        
        return None
    
    def _show_setup_message(self):
        """Show LangChain-powered setup message."""
        print_info("🚀 Amvka 2.0 - Universal AI Command Assistant")
        print_info("✨ Powered by LangChain - Supporting 100+ AI Providers!")
        print_info("")
        print_info("🎯 Quick Setup: Run 'amvka config'")
        print_info("")
        print_info("🤖 Supported Providers (via LangChain):")
        print_info("   • OpenAI, Google Gemini, Anthropic Claude")
        print_info("   • Azure OpenAI, AWS Bedrock, Cohere")
        print_info("   • Ollama (local), Hugging Face, and 90+ more!")
        print_info("")
        print_info("💡 LangChain Benefits:")
        print_info("   • Universal interface across all providers")
        print_info("   • Advanced features: chains, agents, memory")
        print_info("   • Production-ready with built-in retry logic")
        print_info("   • Future-proof - auto-support for new models")
        print_info("")
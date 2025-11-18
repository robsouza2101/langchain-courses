from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")

    # Template to summarize information about a person (ChatOllama)
    # information = """
    # Philippe Coutinho Correia (Rio de Janeiro, 12 de junho de 1992) é um futebolista brasileiro que atua como meio-campista no Vasco da Gama.
    # Uma das grandes revelações do Vasco no século XXI, Philippe Coutinho foi contratado pela Internazionale em 2008, com apenas 16 anos, mas continuou no clube carioca e realizou sua estreia como profissional no ano de 2009. O meia seguiu para a Inter em 2010, após completar 18 anos, mas teve poucas chances e foi emprestado ao Espanyol.
    # Em janeiro de 2013 foi negociado com o Liverpool, onde viveu seu auge e tornou-se um dos melhores jogadores do futebol europeu. Em janeiro de 2018, Coutinho assinou com o Barcelona por 135 milhões de euros, sendo a quarta transferência mais cara da história do futebol. Emprestado ao Bayern de Munique na temporada 2019–20, o meia não foi titular absoluto na equipe, mas era constantemente utilizado e fez parte da conquista da tríplice coroa. Coutinho retornou ao futebol inglês em janeiro de 2022, inicialmente sendo emprestado ao Aston Villa. Após reencontrar o bom futebol na equipe, assinou em definitivo com os Lions.
    # Pela Seleção Brasileira, o jogador estreou em 2010 e disputou mais de 60 partidas. Convocado para três edições da Copa América, foi campeão da competição em 2019, sendo um dos principais destaques do título em solo brasileiro. Além disso, também representou a Amarelinha na Copa do Mundo de 2018.    
    # """
    # summary_template = """
    # Dado a informação: {information} sobre uma pessoa, eu quero que vc elabore:
    # 1. Um resumo curto;
    # 2. Dois fatos interessante sobre essa pessoa.
    # """
    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"],
    #     template=summary_template,
    # )

    # Template to Tavily Search (query)
    query = "Faça um resumo curto e 2 fatos interessantes sobre Philippe Coutinho Correia."

    # Which LLM to use
    llm = TavilySearch(topic="general", max_results=1)
    # llm = ChatOllama(tempeture=0, model="gemma3:270m")
    
    # Response from Tavily Search
    response = llm.invoke({"query": query})
    print("\n🔎 Resultados da pesquisa Tavily:\n")
    for r in response["results"]:
        print(f"- {r['title']}: {r['url']}")
        print(f"  Content: {r['content']}\n")

    # Response from the summary prompt template (Ollama gemma3)
    # chain = summary_prompt_template | llm
    # response = chain.invoke(input={"information": information})
    # print(response.content)


if __name__ == "__main__":
    main()

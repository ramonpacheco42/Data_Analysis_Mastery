# Data_Analysis_Mastery
Curso realizado na plataforma stack academy com opjetivo de realizar um projeto de ponta a ponta usando a metodologia CRISP-DM.

# Como desenvolver um projeto de Data Science com CRISP-DM


# 1. Entendimento do Negócio

Netflix é uma das plataformas de streaming de mídia e vídeo mais populares do mundo. Eles têm mais de 8.000 filmes ou programas de TV disponíveis em sua plataforma. Em meados de 2021, eles superaram 200 milhões de assinantes em todo o mundo.

    Qual o problema que queremos resolver e por que ele é importante?

R: Queremos entender como é a distribuição dos conteúdos em relação aos paises para sugerir conteúdos e identificar oportunidades de negócios

    Quais perguntas precisas responder?
        a) Entender qual conteúdo está disponível em diferentes países
        b) Identificando conteúdo semelhante combinando recursos baseados em texto
        c) Análise de rede de atores/diretores e encontre insights interessantes
        d) A Netflix tem mais foco em programas de TV do que em filmes nos últimos anos

# 2. Entendimento dos dados

Os dados que serão utilizados neste projeto estão disponível neste link

O arquivo netflix_titles.csv contém os seguintes dados

    show_id: identificador único para filme ou seriados
    type: Identifica se é um filme ou seriado
    title: título do filme ou seriado
    director: nome do diretor do filme ou seriado
    cast: (elenco) nome dos atores envolvidos no filme ou seriado
    country: nome do pais onde o filme ou seriado foi produzido ou apresentado
    date_added: data em que o filme ou seriado foi adicionado na Netflix
    release_year: ano de lançamento do filme ou seriado
    rating: orientação parental (https://pt.wikipedia.org/wiki/Orienta%C3%A7%C3%A3o_Parental_de_TV)
    duration: duração do filme em minutos ou números de temporadas
    listed_in: categorias nas quais o filme ou seriado foi listado
    description: a decrição do summary


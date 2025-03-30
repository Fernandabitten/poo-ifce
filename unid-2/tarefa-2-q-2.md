2) Pense em três problemas da vida real que pode-se modular com orientação a objetos e explique o que corresponde a classe, objeto, métodos e parâmetros.
1. **Sistema de Gerenciamento de Pedidos de Comida**:  
     - **Problema:** Um restaurante precisa gerenciar os pedidos dos clientes, incluindo pratos, valores e status. O sistema precisa ser capaz de adicionar e remover itens, atualizar o status e calcular o total de cada pedido. Além de permitir ver os itens incluídos e o status do pedido (se está sendo preparado, se foi entregue, etc.).
    - **Classe**: Pedido
        representa um pedido.
        - **Objeto:**
            pedido1 (Instancia da classe Pedido, representa um pedido específico feito por um cliente. Ex: Pedido: 101 - Cliente: Fernanda)
        - **Métodos:** - permitem interagir com o objeto
            - **`adicionarItem(item, quantidade)`**  
                Adiciona um item ao pedido.
            - **`removerItem(item)`**  
                Remove um item do pedido.
            - **`calcularTotal()`**  
                Calcula o total do pedido.
            - **`alterarStatus()`**  
                Atualiza o status do pedido (ex.: "Em preparo", "Pronto", "Entregue").
        - **Parâmetros:** - permitem armazenar informações sobre o objeto
            - **`cliente`**: Identificação do cliente que fez o pedido.
            - **`data`**: Data em que o pedido foi realizado.
            - **`itens`**: Lista de itens incluídos no pedido.
            - **`total`**: Valor total do pedido.
            - **`novo_status`**:Status do pedido.

2. **Controle de Iluminação em um Escritório**:  
     - **Problema:** Em um escritório, o administrador deseja automatizar o controle das luzes para economizar energia. O sistema deve permitir ligar ou desligar as luzes de diferentes salas, ajustar a intensidade das lâmpadas (se forem dimmers) e verificar o estado atual de cada luz. Além disso, o sistema pode ser configurado para desligar automaticamente as luzes após o horário de expediente.
     
    - **Classe**: Luz
        representa uma lâmpada em uma sala do escritório.
        - **Objeto:**
            luz1 (Instancia da classe Luz, representa uma luz específica em uma sala (exemplo: "Luz da Sala de Reunião")).
        - **Métodos:** - permitem interagir com o objeto
            - **`ligar()`**  
                Altera o estado da luz para ligada.
            - **`desligar()`**  
                Aaltera o estado para desligada.
            - **`ajustar_intensidade(nova_intensidade)`**  
                Define um novo valor para a intensidade da luz.
            - **`verificar_estado()`**  
                Retorna se a luz está ligada ou desligada e qual é sua intensidade.
        - **Parâmetros:** - permitem armazenar informações sobre o objeto
            - **`estado`**: Armazena o estado atual da luz (ligada ou desligada (True para ligada e False para desligada)).
            - **`intensidade`**: Representa a intensidade da luz (exemplo: um valor entre 0 e 100).
            - **`sala`**: Nome da sala onde a luz está localizada (exemplo: "Sala de Reunião").   

3. **Controle de Animais em um petshop**:  
     - **Problema:** Um petshop precisa de um sistema para gerenciar os animais que estão sob seus cuidados. O sistema deve registrar informações sobre os animais, como nome, espécie, raça, idade e histórico. Além disso, o sistema deve permitir agendar serviços para os animais, como banho, tosa e consultas veterinárias. 
    - **Classe**: Animal
        representa um animal em  um petshop.
        - **Objeto:**
            animal1 (Instancia da classe Animal, representa um pet específico atendido no petshop. Exemplo: Lisa uma cadela da raça vira-lata com pastor alemão de 13 anos de idade)
        - **Métodos:** - permitem interagir com o objeto
            - **`atualizar_historico(descricao)`**  
                Adiciona uma nova entrada ao histórico.
            - **`exibir_informacoes()`**  
                Retorna as informações completas do animal.
        - **Parâmetros:** - permitem armazenar informações sobre o objeto
            - **`nome`**: Nome do animal.
            - **`especie`**: Espécie do animal (exemplo: cachorro, gato, pássaro).
            - **`raca`**: Raça do animal.
            - **`idade`**: Idade do animal.
            - **`historico`**: Histórico do animal (exemplo: vacinas aplicadas, doenças tratadas, serviço prestado ao animal (como banho, tosa, etc)).
    
    - **Classe**: Serviço
        representa um serviço.
        - **Objeto:**
            servico1 (Instancia da classe Serviço, representa um serviço específico oferecido pelo petshop (exemplo: banho, tosa ou consulta veterinária)).
        - **Métodos:** - permitem interagir com o objeto
            - **`exibir_detalhes()`**  
                Retorna os detalhes do serviço.
        - **Parâmetros:** - permitem armazenar informações sobre o objeto
            - **`nome`**: Nome do serviço (exemplo: "Banho").
            - **`preco`**: Preço do serviço.
            - **`descrecao`**: Descrição detalhada do serviço.
    
    - **Classe**: Agendamento
        representa um agendamento.
        - **Objeto:**
            agendamento1 (Instancia da classe Agendamento, representa um agendamento específico (exemplo: "Banho para Rex no dia 29/03/2025").).
        - **Métodos:** - permitem interagir com o objeto
            - **`confirmar_agendamento()`**  
                Confirma o agendamento e salva as informações no sistema.
            - **`cancelar_agendamento()`**  
                    Cancela o agendamento.
        - **Parâmetros:** - permitem armazenar informações sobre o objeto
            - **`animal`**: O animal para o qual o serviço foi agendado.
            - **`servico`**: O serviço que será realizado.
            - **`data_hora`**: Data e hora do agendamento.

    A classe Animal é usada para cadastrar e gerenciar informações sobre os animais atendidos no petshop. Por exemplo, "Lisa" seria um objeto da classe Animal com atributos como nome = "Lisa", espécie = "Cachorro", raça = "Vira-lata com pastor alemão", idade = 13 anos.

    A classe Servico é usada para definir os serviços disponíveis no petshop. Por exemplo, "Banho" seria um objeto da classe Servico com atributos como nome = "Banho", preço = R$30, descrição = "Banho completo com shampoo especial".

    A classe Agendamento conecta um objeto da classe Animal a um objeto da classe Servico, indicando quando o serviço será realizado. Por exemplo, um agendamento pode ser criado para marcar um banho para "Lisa" no dia 29/03/2025 às 15h.
    

# Projeto de Cloud 2022.2
## Interface para Infraestrutura AWS com TerraForm

Aluno: Arthur Gomes Chieppe

# A proposta do projeto

Nesse programa, almeja-se tornar o deploy e a gerencia de instancias EC2 na AWS uma tarefa facil, rápida, reproduzível e programática. Para atingir esse objetivo, um programa com CLI em Python foi desenvolvido para abstrair o desenvolvimento de arquivos de configuração do TerraForm.

# Features do programa:

Com esse programa, o usuário é capaz de provisionar instâncias EC2, criar e gerenciar security groups e até mesmo criar e deletar usuários IAM. Além disso, a aplicação também lista todas as características da configuração atualmente existente.

# Requerimentos:

* TerraForm
* Instalar as bibliotecas no requirements.txt
* Ter as credenciais da AWS nas environments variables, como no comando abaixo:

```
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
```

### Caso esteja utilizando o Python 3.10:

Alterar linha no arquivo: 
```
...\.venv\Lib\site-packages\prompt_toolkit\styles\from_dict.py
```
De:
```python
from collections import Mapping
```
Para:
```python 
from collections.abc import Mapping
```

# Uso:

O uso do aplicativo é bem autoexplicativo, já que as opções no terminal são bem descritivas em relação a o que fazem. A navegação pelos menus é feita utilizando as setas do teclado, e a seleção é efetivada com a tecla enter. 



A primeira ação a ser feita no programa é selecionar *Create Whole new Infraestructure*, já que  . Embora intuitivo, o uso do programa requer certa destreza do usuário em relação às configurações do TerraForm, pois inputs de dados errados podem fazer com que o programa não opere como desejado. Quando o usuário ficar preso em uma situação dessas, é recomendado que ele selecione a opção *Create Whole new Infraestructure*.

Nessa opção o usuário pode escolher quantas máquinas *micro* e *medium* ele deseja criar. Os módulos das máquinas criadas terão o padrão de nome a seguir:
```
aws_instance_{type}_{count}" (Ex: aws_instance_micro_0, aws_instance_medium_1, etc)
```
Com esse programa não é possível personalizar configurações de VPC e Subnet, valores escolhidos e que funcionam já foram pré-definidos.

Aṕos a configuração inicial, o usuário pode realizar o seguinte:
* Destruir toda a infraestrutura criada
* Listar toda a infraestrutura criada
* Gerenciar instâncias EC2
* Gerenciar *security groups*
* Gerenciar usuários IAM

## Gerenciar instâncias EC2:

O menu de gerenciar instâncias permite ao usuário adicionar ou remover novas instâncias sem mudar o resto da configuração. Para remover, o programa primeiramente listará todas as instâncias ativas, para ajudar o usuário na sua decisão. Em seguida, o programa perguntará ao usuário o final nome do módulo da instância que deseja remover.
A resposta deve ser o final do nome do módulo. Por exemplo, se o módulo se chama "aws_instance_micro_1", o input do usuário deve ser 
```
micro_1
```
## Gerenciar security groups

O menu de gerenciar security groups permite o usuário criar, deletar, listar e designar um security group a uma instância. Ao deletar, o programa funciona da mesma forma que ao deletar instâncias, perguntando ao usuário o final do nome do módulo do security group que deseja remover. Por exemplo, se o módulo se chama "aws_security_group_mysql", o input do usuário deve ser:
```
mysql
```

Note que para deletar um security group, o usuário deve se certificar que ele não esteja aplicado em nenhuma instância. Caso ele esteja, é necessário apagar a instância em questão, pois o programa permite ao usuário apenas associar um security group a uma instância, sendo a desassociação não é suportada pelo programa.

## Gerenciar usuários IAM

Com esse programa, é possível criar, listar e deletar usuários IAM na AWS a partir do TerraForm. Como de praxe, para deletar é necessário informar o final do nome do módulo do usuário_iam que deseja remover. Por exemplo, se o módulo se chama "aws_security_group_edirmacedo", o input do usuário deve ser:
```
edirmacedo
```

# Troubleshooting:

Em caso de qualquer erro não contemplado pelo programa, recomenda-se que o usuário crie uma nova infraestrutura a partir da seleção *Create whole new infraestructure*. Com essa opção, quaisquer eventuais erros serão sobrescritos.








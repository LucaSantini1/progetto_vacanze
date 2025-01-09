```mermaid
classDiagram
    class Main {
        +main()
    }

    class Fighter {
        +name: String
        +weight_class: String
        +fight(opponent: Fighter, user_control: Boolean): Boolean
    }

    class Tournament {
        +fighters: List<Fighter>
        +tournament(user_fighter: Fighter, fighters: List<Fighter>): Boolean
    }

    Main --> Fighter : fight()
    Main --> Tournament : tournament()
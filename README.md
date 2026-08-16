```
██████╗███████╗██╗  ██╗████████╗███╗   ███╗ ██████╗
╚═██╔═╝██╔════╝╚██╗██╔╝╚══██╔══╝████╗ ████║██╔════╝
  ██║  █████╗   ╚███╔╝    ██║   ██╔████╔██║██║     
  ██║  ██╔══╝   ██╔██╗    ██║   ██║╚██╔╝██║██║     
  ██║  ███████╗██╔╝ ██╗   ██║   ██║ ╚═╝ ██║╚██████╗
  ╚═╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝
```

Text-based Minecraft project written in Python.

## **Features**

- Inventory system with item stacking
- Crafting system
- Tools, blocks and food
- Health and hunger stats
- Tool durability
- Saving and loading with JSON
- Custom exceptions
- Automated tests with pytest

## **Project structure**

```text
TextMC/
├── tests/
│   ├── test_inventory.py
│   ├── test_crafting.py
│   ├── test_persistency.py
│   ├── test_stats.py
│   └── test_loading.py
├── main.py
├── items.py
├── inventory.py
├── crafting.py
├── stats.py
├── persistency.py
├── exceptions.py
├── recipes.json
├── .gitignore
└── README.md
```

## **Run**

```bash
git clone https://github.com/Wolverine021/TextMC.git
cd TextMC
python3 main.py
```

## **Tests**

```bash
python3 -m pytest -v
```

## **Status**

Current version: **v1.0.0**.


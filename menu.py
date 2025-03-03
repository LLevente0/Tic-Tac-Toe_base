def get_menu_option():
    valasztas = int(input("""
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI\n
  Válassz egy módot: """))

    if valasztas < 5:
        return valasztas
    else:
        ValueError
        print("Hiba! Kérlek adj meg egy új számot!")
        get_menu_option()

"""
  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input new value.

  pass
"""

if __name__ == "__main__":
    option = get_menu_option()
    print(option)
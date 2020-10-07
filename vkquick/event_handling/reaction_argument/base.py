class ReactionArgument:
    """
    Аннотация реакции должна быть исключительно этим типом
    """

    always_be_instance = False
    """
    Если в тайпинг передан класс вместо инстанса,
    то при значении `True` `EventHandler`
    создаст инстанс без аргументов. 
    """
import ckan.model as model


def sum_organization():
    '''Vrati pocet organizacii'''

    organizations = model.Session.query(model.Group) \
        .filter(model.Group.type == 'organization') \
        .count()
    return organizations


def sum_group():
    '''Vrati pocet kategorii'''

    groups = model.Session.query(model.Group) \
        .filter(model.Group.type == 'group') \
        .count()
    return groups


def sum_dataset():
    '''Vrati pocet datasetov'''

    # poziadavka z MZV od pana Kovaca
    pripocitaj_dataset = 1

    datasets = model.Session.query(model.Package) \
        .filter(model.Package.state == 'active') \
        .filter(model.Package.private == False) \
        .count()
    return datasets + pripocitaj_dataset


def sum_resource():
    '''Vrati pocet datovych zdrojov'''
    resources = model.Session.query(model.Resource) \
        .filter(model.Resource.state == 'active') \
        .count()
    return resources


def declension_dataset():
    '''Vrati spravny tvar slova dataset podla poctu datasetov'''

    datasets = sum_dataset()
    if datasets == 1:
        word = "Dataset"
    elif datasets >= 2 and datasets <= 4:
        word = "Datasety"
    else:
        word = "Datasetov"
    return word


def declension_group():
    '''Vrati spravny tvar slova kategoria podla poctu kategorii'''

    groups = sum_group()
    if groups == 1:
        word = "Kategória"
    elif groups >= 2 and groups <= 4:
        word = "Kategórie"
    else:
        word = "Kategórií"
    return word


def api_resource_id():
    '''Vrati resource_id - teraz Zoznam datasetov v správe MZVaEZ SR'''
    resource_id = 'f2de4752-6d42-4271-bbbc-4ce2d85a730a'  # Rozpočet podľa funkčnej klasifikácie
    return resource_id

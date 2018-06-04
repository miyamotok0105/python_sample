import xml.etree.ElementTree as ET

from rx import Observable


def log(item):
    print(item)


def xml(item):
    """
    Open xml file
    :param item:
    :return: country nodes
    """
    # todo: validate xml
    tree = ET.parse(item)
    return tree.getroot().findall('country')


def normalize(item):
    """
    Normalize XML elements.
    :param item:
    :return: Simple dict
    """
    # example: try to find case insensitive rank
    rank = 0
    for feat in item:
        if feat.tag.lower() == 'rank':
            rank = int(feat.text)
            break

    return {
        'name': item.get('name'),
        'rank': rank
    }


def rank_filter(item):
    """
    Filter countries with rank < 10
    :param item:
    :return:
    """
    return item['rank'] >= 10


xs = Observable.from_(['003file1.xml'])
xs.flat_map(xml) \
    .map(normalize) \
    .filter(rank_filter) \
    .subscribe(log)
""" Module contains database functions"""
# coding: utf-8

from tinydb import TinyDB, Query


q = Query()


def access_db(path):
    db = TinyDB(path)
    return db


def query():
    return Query()


def max_id(db):
    """Define maximum item's id"""
    i = 0
    for item in db:
        if item['id'] > i:
            i = item['id']
    return i


def add_item_db(item, db):
    db.insert(item)


def search_db(id, db):
    try:
        search = db.search(q.id == id)[0]
        reponse = search
    except IndexError:
        reponse = False
    return reponse


def update_item_in_db(db, key, info_modify, id):
    db.update({key: info_modify}, q.id == id)


def remove_in_db(db, id):
    db.remove(q.id == id)

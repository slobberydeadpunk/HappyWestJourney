from Role import Role

def test_role():
    r = Role(10000, 20000)
    print str(r)
    r.rem_health(100)
    print str(r)
    r.add_health(200)
    print r
    print r.is_alive()
    r.rem_health(10000)
    print r.is_alive()

if __name__ == "__main__":
    test_role()

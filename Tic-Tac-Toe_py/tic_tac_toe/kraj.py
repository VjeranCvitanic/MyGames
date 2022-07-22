def igra_gotova(m):                                                     #provjerava je li igra gotova

    a = 0
    b = 0

    while(a<3):
        if m[a][b] == m[a][b+1] and m[a][b] == m[a][b+2] and m[a][b] != " ":
            return m[a][b]
        a=a+1

    a = 0
    while (b < 3):
        if m[a][b] == m[a+1][b] and m[a][b] == m[a+2][b] and m[a][b] != " ":
            return m[a][b]
        b=b+1

    b = 0

    if m[0][0] == m[1][1] == m[2][2] != " ":
        return m[1][1]

    elif m[0][2] == m[1][1] == m[2][0] != " ":
        return m[1][1]

    elif m[0][0] != " " and  m[0][1] != " " and m[0][2] != " " and  m[1][0] != " " and m[1][1] != " " and  m[1][2] != " " and m[2][0] != " " and  m[2][1] != " " and m[2][2] != " " :
        return 1
    else:
        return 0







"""def igra_gotova(m):                                                     #provjerava je li igra gotova

    a = 0
    b = 0

    while(a<3):
        if m[a][b] == m[a][b+1] and m[a][b] == m[a][b+2] and m[a][b] != " ":
            return m[a][b]
        a=a+1

    a = 0
    while (b < 3):
        if m[a][b] == m[a+1][b] and m[a][b] == m[a+2][b] and m[a][b] != " ":
            return m[a][b]
        b=b+1

    b = 0

    if m[0][0] == m[1][1] == m[2][2] != " ":
        return m[1][1]

    elif m[0][2] == m[1][1] == m[2][0] != " ":
        return m[1][1]

    elif m[0][0] != " " and  m[0][1] != " " and m[0][2] != " " and  m[1][0] != " " and m[1][1] != " " and  m[1][2] != " " and m[2][0] != " " and  m[2][1] != " " and m[2][2] != " " :
        return 1
    else:
        return 0"""











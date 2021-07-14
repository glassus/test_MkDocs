 Merci Francky !

# fdsfj

## Premier test

Il semblerait que ça marche...


bien ?

{{ terminal() }}

$f(x)= \frac{x}{2}+5$



??? tip "indices"
    === "fidn"
        blabla

    === "fsjdlk"
        dfks,jlkf
    
    === "fsdlkfl"
        kdlfnln


[Combien y a-t-il de triangles sur cette figure ?](#réponses){ .md-button }


!!! Abstract "En résumé"
    Ce problème sera ensuite résolu de manière progressive, et c'est l'occasion d'utiliser :

    - des méthodes par 



!!! warning "Attention"
    Un exercice est inclus dans le script ci-dessous.


```python
def ens_triangle(n):
    """Renvoie l'ensemble des points
       - à coordonnées entières ;
       - inclus dans le triangle de côté n.
    """
    points = {}
    for i in range(n+1):
        for j in range(n+1):
            if i + j <= n:
                points.add( (i, j) )
    return points
```

## Réponses aux problèmes <a name="réponses"></a>

??? done "Réponses"
    === "_Problème_"
        Vous pouvez obtenir la réponse, mais avez-vous bien cherché avant ?

    === "Triangle ; $n=6$"
        Il y a $78$ triangles.

    === "Rectangle ; $n=6$ et $m=10$"
        Il y a $1155$ rectangles.
    
    === "Hexagone ; $n=5$"
        Il y a $496$ triangles.

    === "Hexagone étoilé ; $n=3$"
        Il y a $354$ triangles.

# fdsj

## test abréviations

Il suffit de faire comme ça

*[suffit]: c'est vite dit

et voilà.

## admonitions

???+ note
    fdsfjlk
    fdsjflk
    dskfl


vd

!!! info inline end
    fdjslkfs
    sdfkjdlk
    sdfklj

fjsdlfk


| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |




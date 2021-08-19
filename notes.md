# Flask_SQLAlchemy

## Connection URI

  - Las (3) '///' es una instruccion de que la db se guarde en el mismo directorio del proyecto
  - Las (4) '////' en Unix/Mac

  - Windows (note 3 leading forward slashes and backslash escapes)
    "sqlite:///C:\\absolute\\path\\to\\foo.db"

    Windows **(alternative using raw string)**
    "r'sqlite:///C:\absolute\path\to\foo.db'"

## Creando una nueva tabla
  - Para manejar una sintaxis correcta del lenguaje en el uso de ORM las tablas se interpretan a traves de modelos. 
  - En flask_sqlalchemy se crean los modelos con clases. Ej:
    
    ```
    class Empresa(db.Model):
          id = db.Column(db.Integer, primary_key=True)
          nombre = db.Column(db.String(20))
          fundaction = db.Column(db.Integer, nullable=True)
    ```
  
## Insertar data por medio de los modelos
  1. importamos primero db de app
  2. importamos el modelo para el caso de ejemplo Empresa
  3. Instanciamos los datos a traves del modelo. ejem:
    ```
    empresa1 = Empresa(nombre='Google', fundaction=1998)
    empresa2 = Empresa(nombre='Apple', fundaction=1975)
    empresa3 - Empresa(nombre='Facebook', fundaction=2004)

    db.session.add(empresa1)
    db.session.add(empresa2)
    db.session.add(empresa3)
    ```
  4. Hacemos un commit para que los datos insertados por medio del modelo se inserten en la base de datos
    ```
    db.session.commit()
    ```

## Ver, eliminar y modificar datos
  - Podemos consultar, modificar o eliminar los datos
    ```
    # Consultar datos
    empresa1.nombre
    'Google'
    empresa1.fundaction
    1998

    # Modificar datos
    empresa1.fundaction = 2000
    empresa1.fundaction
    '2000'
    empresa2.nombre = 'Apppple'
    empresa2.nombre
    'Apppple'

    # Eliminar datos
    db.session.delete(empresa2)
    db.session.commit()
    ```
  - Podemos consultar o listar todas las listas que se han registrado a traves del modelo

    ```
    Empresa.query.all()
    <Empresa 1>, <Empresa 2>
    ```
    - Para que nos represente nuestras listas con un nombre representativo y no con un nombre generico colocamos en el codigo

      ```
      def __repr__(self):
          return f'{self.nombre}'
      ```

    - Entonces tendremos como resultado en la consulta de los datos
    
      ```
      Empresa.query.all()
      [Google, Facebook]
      ```

## Claves foraneas o claves primarias y secundarias

  - Es necesario que nuestros modelos cuenten con primery_key
  - Para relaciones de muchos a muchos se debe crear una tabla que relacione los modelos
    - donde las columnas de esta tabla relacionadora seran las claves primarias de los modelos a relacionar
      > Mirar codigo
## Crear Datos o llenar la db

  Aca algunos datos para pruebas:
  ```
  google = Empresa(nombre='Google', fundacion=1998)
  microsoft = Empresa(nombre='Microsoft', fundacion=1975)
  apple = Empresa(nombre='Apple', fundacion=1975)
  amazon = Empresa(nombre='Amazon', fundacion=1999)
  ebay = Empresa(nombre='Ebay', fundacion=1997)
  facebook = Empresa(nombre='Facebook', fundacion=2004)
  twitter = Empresa(nombre='Twitter', fundacion=2009)
  yahoo = Empresa(nombre='Yahoo', fundacion=1996)
  snapchat = Empresa(nombre='Snapchat', fundacion=2012)
  instagram = Empresa(nombre='Instagram', fundacion=2010)

  db.session.add(google)
  db.session.add(microsoft)
  db.session.add(apple)
  db.session.add(amazon)
  db.session.add(ebay)
  db.session.add(facebook)
  db.session.add(twitter)
  db.session.add(yahoo)
  db.session.add(snapchat)
  db.session.add(instagram)

  java = Lenguaje(nombre='java', creador='James Gosling')
  c = Lenguaje(nombre='c', creador='Dennis Ritchie')
  python = Lenguaje(nombre='python', creador='Guido Van Rossum')
  haskell = Lenguaje(nombre='haskell')
  javascript = Lenguaje(nombre='javascript', creador='Brendan Eich')
  basic = Lenguaje(nombre='basic', creador='John G. Kemeny')
  cplusplus = Lenguaje(nombre='c++', creador='Bjarne Stroustrup')
  csharp = Lenguaje(nombre='c#')
  swift = Lenguaje(nombre='swift', creador='Chris Lattner')
  kotlin = Lenguaje(nombre='kotlin')

  db.session.add(java)
  db.session.add(c)
  db.session.add(python)
  db.session.add(haskell)
  db.session.add(javascript)
  db.session.add(basic)
  db.session.add(cplusplus)
  db.session.add(csharp)
  db.session.add(swift)
  db.session.add(kotlin)

  john = Programador(nombre='Jonh', edad=22, empresa=apple)
  juan = Programador(nombre='Juan', edad=22, empresa=apple)
  jose = Programador(nombre='Jose', edad=25, empresa=twitter)
  edgar = Programador(nombre='Edgar', edad=26, empresa=twitter)
  mark = Programador(nombre='Mark', edad=26, empresa=facebook)
  venus = Programador(nombre='Venus', edad=28, empresa=snapchat)
  sol = Programador(nombre='Sol', edad=28, empresa=snapchat)
  andrea = Programador(nombre='Andrea', edad=29, empresa=yahoo)
  cardi = Programador(nombre='Cardi', edad=23, empresa=amazon)
  maria = Programador(nombre='Maria', edad=23, empresa=google)
  joel = Programador(nombre='Joel', edad=24, empresa=google)
  salman = Programador(nombre='Salman', edad=25, empresa=google)
  tabata = Programador(nombre='Tabata', edad=27, empresa=ebay)

  db.session.add(john)
  db.session.add(juan)
  db.session.add(jose)
  db.session.add(edgar)
  db.session.add(mark)
  db.session.add(venus)
  db.session.add(sol)
  db.session.add(andrea)
  db.session.add(cardi)
  db.session.add(maria)
  db.session.add(joel)
  db.session.add(salman)
  db.session.add(tabata)

  db.session.commit()
  ```

## Querys con datos

  - Como seleccionar todos los elementos de una tabla de la db
    ```
    >>> Empresa.query
    # Objeto no interpretado
    <flask_sqlalchemy.BaseQuery object at 0x7fa270013190>

    >>> Empresa.query.all()
    # Listado de objetos referenciados guardados en la tabla
    [Google, Microsoft, Apple, Amazon, Ebay, , Facebook, Twitter, Yahoo, Snapchat, Instagram]

    >>> Programador.query.all()[:5]
    # Slice de lista de los 5 ultimos valores 
    [John, Juan, Jose, Edgar, Mark]
    ```
  - Como seleccionar solo el primer valor
    ```
    >>>Programador.query.first()
    John
    ```
  - Buscar datos en especifico
    ```
    >>> Empresa.query.filter(Empresa.nombre=='Google').first()
    Google

    >>> Empresa.query.filter(Empresa.id==2).first()
    Microsoft

    >>> Empresa.query.filter(Empresa.nombre != 'Google').all()
    [Microsoft, Apple, Amazon, Ebay, Facebook, Twitter, Yahoo, Snapchat, Instagram]

    # Si queremos un dato sin importar mayusculas o minusculas usamos like
    >>> Empresa.query.filter(Empresa.nombre.like('%google%')).first()
    Google

    >>> Programador.query.filter(Programador.edad >= 25).all()
    # Regresa todos los programadores con edad mayores iguales a 25

    >>> Programador.query.filter(Programador.nombre.in_(['Joel', 'Jose', 'Jaime'])).all()
    # Regresa valores que tengan el listado de valores en in
    ['Jose', 'Joel']

    >>> Programador.query.filter(~Programador.nombre.in_(['Joel', 'Jose', 'Jaime'])).all()
    # Regresa todos los datos menos los que estan en el listado de in
    ```
    >  con el signo '~' niega la sentencia que se este usando en el filtro
    ```
    >>> Lenguaje.query.filter(Lenguaje.creador == None).all()
    # Regresa todos los valores que no tengan valor en el campo "creador"
    ```
  - Usando operadores 'AND'
    ```
    >>> Programador.query.filter(Programador.edad >= 23, Programador.nombre == 'Jose').first()
    # Regresa valores programadores con edad mayor igual a 23 y que su nombre sea "Jose"  
    Jose
    ```
    > Usando ',' como 'AND'
    ```
    >>> Programador.query.filter(Programador.edad >= 23).filter(Programador.nombre == 'Jose').first()
    ```
    > Otra manera de usar dos condiciones con "AND" es concatenando los filtros
  - Contar datos registrados en una tabla
    ```
    >>> Programador.query.count()
    13
    >>> Empresa.query.count()
    10
    ```
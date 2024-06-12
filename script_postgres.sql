--Script creación de tablas

CREATE TABLE Usuario (
    id_usuario SERIAL PRIMARY KEY,
    usuario VARCHAR(64) UNIQUE NOT NULL,
    contrasena VARCHAR(256) NOT NULL
);

CREATE TABLE Tarea (
    id_tarea SERIAL PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    descripcion VARCHAR(120) NOT NULL,
    fecha_creacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario)
);
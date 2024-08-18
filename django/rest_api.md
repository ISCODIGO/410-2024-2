# REST API (Representational State Transfer Application Programming Interface)

Una **REST API** es un conjunto de reglas y convenciones que permite la comunicación entre sistemas a través de **HTTP**, utilizando operaciones básicas como `GET`, `POST`, `PUT`, `DELETE`, entre otras. REST es un estilo arquitectónico que se basa en **recursos**, los cuales son representados mediante **URLs**. Cada recurso puede ser manipulado usando métodos HTTP, y las respuestas suelen estar en formato **JSON** o **XML**.

## Características principales de una REST API

1. **Stateless**: Cada solicitud de cliente a servidor debe contener toda la información necesaria para entender y procesar la solicitud, sin depender de ningún estado almacenado en el servidor.
2. **Client-Server**: Separa la interfaz de usuario (cliente) de los datos y la lógica del servidor, permitiendo que ambos evolucionen de manera independiente.
3. **Cacheable**: Las respuestas deben indicar si son cacheables o no, para mejorar la eficiencia mediante la reutilización de respuestas anteriores.
4. **Uniform Interface**: La interfaz es consistente, proporcionando una manera estándar de interactuar con los recursos, lo que simplifica la comunicación entre diferentes partes del sistema.
5. **Layered System**: La arquitectura puede estar compuesta de capas que funcionan juntas, lo que permite, por ejemplo, la introducción de proxies y gateways para mejorar la escalabilidad.

## Operaciones comunes

- **GET**: Recupera una representación de un recurso.
- **POST**: Crea un nuevo recurso.
- **PUT**: Actualiza un recurso existente, reemplazando completamente su representación.
- **PATCH**: Actualiza parcialmente un recurso existente, modificando solo los campos específicos que se envían en la solicitud.
- **DELETE**: Elimina un recurso.

## Diferencia entre PUT y PATCH

- **PUT**: Se utiliza para **reemplazar completamente** un recurso. Esto significa que si un recurso tiene varios campos y envías una solicitud `PUT` con solo algunos de esos campos, los campos no incluidos en la solicitud se eliminarán o restablecerán a su valor por defecto.
  
  Ejemplo:
  - `PUT /usuarios/1`
    ```json
    {
      "nombre": "Juan",
      "edad": 30
    }
    ```
  Esto reemplazará completamente la representación del usuario con ID 1.

- **PATCH**: Se utiliza para **modificar parcialmente** un recurso. Solo los campos especificados en la solicitud `PATCH` se actualizarán, y los demás campos del recurso permanecerán intactos.
  
  Ejemplo:
  - `PATCH /usuarios/1`
    ```json
    {
      "edad": 31
    }
    ```
  Esto solo actualizará el campo `edad` del usuario con ID 1, manteniendo los demás campos sin cambios.

## Idempotencia

- **Idempotentes**: Los métodos `GET`, `PUT`, `PATCH`, y `DELETE` son idempotentes. Esto significa que realizar la misma solicitud varias veces tendrá el mismo efecto que realizarla una sola vez.
  - **GET**: Siempre retorna el mismo recurso.
  - **PUT**: Reemplazar un recurso con la misma representación varias veces no cambia el resultado.
  - **PATCH**: Aplicar los mismos cambios parciales varias veces no cambia el resultado final.
  - **DELETE**: Eliminar un recurso varias veces es lo mismo que eliminarlo una sola vez (si no existe, simplemente retorna una respuesta indicando que el recurso no se encontró).

- **No idempotente**: El método `POST` no es idempotente. Cada vez que se realiza una solicitud `POST`, generalmente se crea un nuevo recurso, lo que significa que repetir la solicitud puede tener un efecto diferente (por ejemplo, crear múltiples recursos).

## Ejemplo de uso

Si tienes un recurso llamado `usuarios`, podrías tener las siguientes rutas:

- `GET /usuarios` - Listar todos los usuarios.
- `POST /usuarios` - Crear un nuevo usuario.
- `GET /usuarios/{id}` - Obtener un usuario específico.
- `PUT /usuarios/{id}` - Reemplazar un usuario específico.
- `PATCH /usuarios/{id}` - Modificar parcialmente un usuario específico.
- `DELETE /usuarios/{id}` - Eliminar un usuario específico.

---

Las REST APIs son ampliamente utilizadas por su simplicidad, escalabilidad y facilidad de uso, permitiendo la interoperabilidad entre diferentes aplicaciones y servicios.

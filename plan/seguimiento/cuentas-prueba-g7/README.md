# Cuentas de prueba G7 para H4

`g7-h4-cuentas.enc` contiene el JSON de cuentas de prueba cifrado con AES-256-GCM. La contraseña se comparte fuera del repositorio. No subir el JSON descifrado ni copiar sus claves a issues, PR o logs.

Para usarlo en una laptop con Python:

```powershell
python -m pip install cryptography
python plan/seguimiento/cuentas-prueba-g7/descifrar.py
```

El script pide la contraseña sin mostrarla y deja el JSON en `.local-private/g7-h4-cuentas.json`, ruta ignorada por Git. El agente puede leer ese archivo local para las pruebas y debe evitar imprimir contraseñas, tokens o códigos MFA.

Para ejecución automática, el agente puede definir `G7_H4_PASSPHRASE` sólo durante el proceso de descifrado y quitarla después. No guardar esa variable en archivos de configuración ni en el repositorio.

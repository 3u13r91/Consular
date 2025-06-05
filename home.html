<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Acceso a Trámites Consulares</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            /* Colores de la Bandera de España como base del diseño */
            --rojo-bandera: #AA151B; /* Rojo intenso */
            --amarillo-bandera: #F1BF00; /* Amarillo brillante */
            --gris-fondo: #F8F8F8; /* Un gris muy claro para el fondo, suave */
            --gris-texto: #333333; /* Gris oscuro para el texto principal */
            --gris-borde-claro: #E0E0E0; /* Gris para bordes sutiles */
            --sombra-clara: rgba(0, 0, 0, 0.08); /* Sombra suave */
            --sombra-media: rgba(0, 0, 0, 0.12); /* Sombra un poco más pronunciada en hover */
            --transicion-suave: 0.3s ease;

            /* Colores y animación para la carga MD3 Expressive */
            --md-sys-color-primary: var(--rojo-bandera); /* Usamos el rojo de la bandera para el spinner */
            --md-sys-color-on-surface-variant: #616161; /* Color para el texto de carga */
            --md-sys-motion-easing-standard: cubic-bezier(0.0, 0.0, 0.2, 1.0);
            --md-sys-motion-easing-decelerate: cubic-bezier(0.0, 0.0, 0.2, 1.0);
            --md-sys-motion-duration-long: 400ms;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: var(--gris-fondo);
            color: var(--gris-texto);
            text-align: center;
            padding: 20px;
            box-sizing: border-box;
            overflow: hidden; /* Evita el scroll cuando el overlay está activo */
        }

        .container {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 6px 15px var(--sombra-clara);
            padding: 40px;
            max-width: 600px;
            width: 100%;
            border: 1px solid var(--gris-borde-claro);
            transition: box-shadow var(--transicion-suave);
        }

        .container:hover {
            box-shadow: 0 8px 20px var(--sombra-media);
        }

        .logo-container {
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--gris-borde-claro);
        }

        .logo {
            max-width: 220px;
            height: auto;
            display: block;
            margin: 0 auto;
        }

        h1 {
            color: var(--gris-texto);
            font-size: 2.3em;
            font-weight: 600;
            margin-bottom: 15px;
            line-height: 1.2;
        }

        p {
            font-size: 1.1em;
            line-height: 1.7;
            margin-bottom: 35px;
            color: var(--gris-texto);
            font-weight: 400;
        }

        .button {
            display: inline-block;
            padding: 14px 28px;
            background-color: var(--rojo-bandera);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1.05em;
            transition: background-color var(--transicion-suave), transform var(--transicion-suave), box-shadow var(--transicion-suave);
            box-shadow: 0 3px 6px var(--sombra-clara);
            cursor: pointer; /* Indica que es clickable */
        }

        .button:hover {
            background-color: color-mix(in srgb, var(--rojo-bandera) 85%, black);
            transform: translateY(-2px);
            box-shadow: 0 5px 10px var(--sombra-media);
        }

        .button:active {
            transform: translateY(0);
            box-shadow: 0 2px 4px var(--sombra-clara);
        }

        .color-accent {
            color: var(--rojo-bandera);
            font-weight: 600;
        }

        /* --- Estilos de la Animación de Carga --- */
        .loading-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.95); /* Fondo blanco semi-transparente */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            visibility: hidden;
            transition: opacity var(--md-sys-motion-duration-long) var(--md-sys-motion-easing-decelerate), visibility 0s linear var(--md-sys-motion-duration-long);
            z-index: 100;
        }

        .loading-overlay.active {
            opacity: 1;
            visibility: visible;
            transition: opacity var(--md-sys-motion-duration-long) var(--md-sys-motion-easing-standard);
        }

        .spinner {
            width: 60px;
            height: 60px;
            border: 6px solid var(--gris-borde-claro); /* Color base del spinner */
            border-top-color: var(--md-sys-color-primary); /* Color principal del spinner */
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Sombra sutil para el spinner */
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .loading-message {
            font-size: 1.2em;
            color: var(--md-sys-color-on-surface-variant);
            font-weight: 500;
        }

        @media (max-width: 600px) {
            .container {
                padding: 30px;
                border-radius: 10px;
            }

            .logo {
                max-width: 180px;
            }

            h1 {
                font-size: 1.8em;
            }

            p {
                font-size: 1em;
            }

            .button {
                padding: 12px 24px;
                font-size: 1em;
            }

            .spinner {
                width: 50px;
                height: 50px;
                border-width: 5px;
            }

            .loading-message {
                font-size: 1em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Logotipo_del_Gobierno_de_Espa%C3%B1a.svg" alt="Logotipo del Gobierno de España" class="logo">
        </div>
        <h1>Acceso a <span class="color-accent">Trámites Consulares</span></h1>
        <p>Para acceder a la página oficial de <strong>Trámites Consulares</strong>, por favor, haga clic en el siguiente enlace:</p>
        <button id="redirectButton" class="button">Acceder a Trámites Consulares</button>
    </div>

    <div id="loadingOverlay" class="loading-overlay">
        <div class="spinner"></div>
        <div class="loading-message">Cargando...</div>
    </div>

    <script>
        document.getElementById('redirectButton').addEventListener('click', function() {
            // Muestra el overlay de carga
            document.getElementById('loadingOverlay').classList.add('active');

            // Redirige después de un pequeño retraso para que se vea la animación
            setTimeout(function() {
                window.location.href = 'https://sutramiteconsular.maec.es/';
            }, 100); // Redirige después de 1 segundo
        });
    </script>
</body>
</html>

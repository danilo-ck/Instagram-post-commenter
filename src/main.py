import instaloader
import time
import random
import sys
from datetime import datetime
from instaloader.structures import Post
from config import USERNAME, PASSWORD, POST_URL, COMMENT_TEXT

print(f"Versión de Instaloader: {instaloader.__version__}")

def init_instagram():
    L = instaloader.Instaloader()
    print('Iniciando sesión...')
    try:
        L.login(USERNAME, PASSWORD)
        print('Login exitoso')
        return L
    except instaloader.TwoFactorAuthRequiredException:
        print('Autenticación de dos factores requerida.')
        two_factor_code = input('Código de dos factores: ')
        L.two_factor_login(two_factor_code)
        return L
    except instaloader.BadCredentialsException:
        print('Error: Usuario o contraseña incorrectos')
        sys.exit(1)
    except Exception as e:
        print(f'Error al iniciar sesión: {str(e)}')
        sys.exit(1)

def get_post(L, post_url):
    try:
        post_code = post_url.split("/p/")[1].split("/")[0]
        return Post.from_shortcode(L.context, post_code)
    except Exception as e:
        print(f'Error al obtener el post: {str(e)}')
        sys.exit(1)

def comment_on_post(L, post, text):
    """Intenta comentar usando la API directa"""
    try:
        endpoint = f"web/comments/{post.mediaid}/add/"
        data = {
            'comment_text': text,
            'replied_to_comment_id': ''
        }
        return L.context._session.post(
            f"https://www.instagram.com/api/v1/{endpoint}",
            data=data
        )
    except Exception as e:
        raise e

def main():
    L = init_instagram()
    post = get_post(L, POST_URL)
    comment_count = 0
    
    print('Iniciando comentarios automáticos...')
    print(f'Post objetivo: {POST_URL}')
    print(f'Comentario a publicar: {COMMENT_TEXT}')
    
    while True:
        try:
            response = comment_on_post(L, post, COMMENT_TEXT)
            if response.status_code == 200:
                comment_count += 1
                wait_time = random.randint(60, 600)
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f'[{current_time}] Comentario #{comment_count} publicado. Esperando {wait_time/60:.1f} minutos...')
                
                if comment_count % 8 == 0:
                    extra_wait = random.randint(300, 480)
                    print(f'Pausa de seguridad adicional de {extra_wait/60:.1f} minutos...')
                    time.sleep(extra_wait)
                
                time.sleep(wait_time)
            else:
                print(f'Error al comentar. Código de estado: {response.status_code}')
                print(f'Respuesta: {response.text}')
                time.sleep(300)  # Esperar 5 minutos antes de reintentar
            
        except instaloader.ConnectionException:
            print('Error de conexión. Esperando 5 minutos...')
            time.sleep(300)
        except Exception as e:
            print(f'Error al comentar: {str(e)}')
            error_wait = random.randint(300, 600)
            print(f'Esperando {error_wait/60:.1f} minutos antes de reintentar...')
            time.sleep(error_wait)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nScript detenido por el usuario')
        sys.exit(0)


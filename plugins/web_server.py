from aiohttp import web
from database.database import db
from config import FREE_SESSION_DURATION
import logging

logger = logging.getLogger(__name__)

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    """Route racine pour vérifier que le serveur fonctionne"""
    return web.json_response({
        "status": "running",
        "bot": "File Store Bot",
        "adsgram": "enabled"
    })

@routes.get("/adsgram/reward")
async def adsgram_reward_handler(request):
    """
    Endpoint appelé par AdsGram quand un utilisateur termine une pub
    URL configurée sur AdsGram: https://test-cey.onrender.com/adsgram/reward?userid=[userId]
    """
    try:
        # Récupérer l'user_id depuis les paramètres de l'URL
        user_id = request.query.get('userid')
        
        if not user_id:
            logger.error("AdsGram reward: userid manquant")
            return web.json_response(
                {"status": "error", "message": "userid required"},
                status=400
            )
        
        try:
            user_id = int(user_id)
        except ValueError:
            logger.error(f"AdsGram reward: userid invalide: {user_id}")
            return web.json_response(
                {"status": "error", "message": "invalid userid"},
                status=400
            )
        
        # Vérifier si l'utilisateur peut regarder une pub
        can_watch = await db.can_watch_ad(user_id)
        
        if not can_watch:
            logger.warning(f"AdsGram reward: utilisateur {user_id} a déjà une session récente")
            # On retourne quand même success pour AdsGram, mais on n'active pas de nouvelle session
            return web.json_response(
                {
                    "status": "success",
                    "message": "session already active",
                    "user_id": user_id
                }
            )
        
        # Activer la session gratuite
        await db.set_free_session(user_id, FREE_SESSION_DURATION)
        
        logger.info(f"✅ AdsGram: Session activée pour l'utilisateur {user_id} via webhook")
        
        # Répondre à AdsGram que tout s'est bien passé
        return web.json_response({
            "status": "success",
            "message": "reward granted",
            "user_id": user_id,
            "duration_hours": FREE_SESSION_DURATION
        })
        
    except Exception as e:
        logger.error(f"Erreur dans adsgram_reward_handler: {e}")
        return web.json_response(
            {"status": "error", "message": str(e)},
            status=500
        )

@routes.get("/adsgram/test")
async def adsgram_test_handler(request):
    """
    Endpoint de test pour vérifier que le webhook fonctionne
    Test: https://test-cey.onrender.com/adsgram/test?userid=123456789
    """
    try:
        user_id = request.query.get('userid')
        
        if not user_id:
            return web.json_response({
                "status": "info",
                "message": "Add ?userid=YOUR_ID to test",
                "example": "https://test-cey.onrender.com/adsgram/test?userid=123456789"
            })
        
        try:
            user_id = int(user_id)
        except ValueError:
            return web.json_response({
                "status": "error",
                "message": "userid must be a number"
            }, status=400)
        
        # Vérifier l'état de la session
        has_session = await db.has_active_session(user_id)
        can_watch = await db.can_watch_ad(user_id)
        session = await db.get_user_session(user_id)
        
        return web.json_response({
            "status": "success",
            "user_id": user_id,
            "has_active_session": has_session,
            "can_watch_ad": can_watch,
            "session_data": {
                "has_free_session": session.get('has_free_session') if session else False,
                "session_expiry": session.get('session_expiry') if session else None,
                "last_ad_watch": session.get('last_ad_watch') if session else None
            }
        })
        
    except Exception as e:
        logger.error(f"Erreur dans adsgram_test_handler: {e}")
        return web.json_response({
            "status": "error",
            "message": str(e)
        }, status=500)

async def web_server():
    """Crée et retourne l'application web aiohttp"""
    web_app = web.Application()
    web_app.add_routes(routes)
    return web_app
DEFAULT_LANG = "fr"

LANGUAGE_NAMES = {
    "fr": "Français 🇫🇷",
    "en": "English 🇬🇧",
    "es": "Español 🇪🇸",
    "de": "Deutsch 🇩🇪",
}

TRANSLATIONS = {
    "fr": {
        "help": (
            "Salut 👋 Je suis ton assistant de suivi de prix Amazon : "
            "je surveille les produits que tu m'indiques et je te préviens dès que leur prix change.\n\n"
            "/track <url> - suivre un produit\n"
            "/list - voir mes produits suivis\n"
            "/untrack <id> - arrêter de suivre un produit\n"
            "/history - consulter l'historique d'un produit\n"
            "/language - changer de langue\n\n"
            "/help - afficher cette aide"
        ),
        "menu_track": "🔍 Suivre un produit",
        "menu_list": "📋 Mes produits",
        "menu_help": "❓ Aide",
        "menu_language": "🌐 Langue",
        "menu_history": "📈 Historique",
        "ask_link": "📋 Colle le lien du produit Amazon à suivre ci-dessous.",
        "fetching": "Récupération du prix en cours...",
        "scrape_failed": "Je n'ai pas réussi à récupérer le prix de ce produit. Vérifie le lien.",
        "product_added": "Produit ajouté (#{id}) : {title}\n\n💰 Prix actuel : {price:.2f}",
        "view_product": "🔗 Voir le produit",
        "delete_product": "🗑 Supprimer ❌",
        "history_button": "📈 Historique",
        "list_empty": "Tu ne suis aucun produit pour l'instant.",
        "list_end": "Fin de la liste.",
        "product_line": "#{id} - {title}\n\n💰 Prix actuel : {price:.2f}",
        "untrack_usage": "Usage : /untrack <id>",
        "untrack_invalid_id": "L'id doit être un nombre.",
        "untrack_not_found": "Produit introuvable.",
        "untrack_not_found_button": "Produit introuvable ou déjà supprimé.",
        "untrack_success": "Produit #{id} supprimé.",
        "untrack_success_button": "Produit #{id} supprimé : {title}",
        "price_drop": "Baisse de prix",
        "price_rise": "Hausse de prix",
        "price_alert": "{direction} ! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Une erreur est survenue, réessaie.",
        "choose_language": "🌐 Choisis ta langue :",
        "language_set": "Langue mise à jour : {name}",
        "history_empty": "Aucun changement de prix à ce jour pour {title}.",
        "history_header": "Historique des prix — {title} :",
        "history_line": "{date} : {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Choisis un produit pour voir son historique :",
    },
    "en": {
        "help": (
            "Hi 👋 I'm your Amazon price-tracking assistant: "
            "I watch the products you give me and notify you whenever their price changes.\n\n"
            "/track <url> - track a product\n"
            "/list - view your tracked products\n"
            "/untrack <id> - stop tracking a product\n"
            "/history - view a product's price history\n"
            "/language - change language\n\n"
            "/help - show this help"
        ),
        "menu_track": "🔍 Track a product",
        "menu_list": "📋 My products",
        "menu_help": "❓ Help",
        "menu_language": "🌐 Language",
        "menu_history": "📈 History",
        "ask_link": "📋 Paste the Amazon product link to track below.",
        "fetching": "Fetching the price...",
        "scrape_failed": "I couldn't fetch the price for this product. Check the link.",
        "product_added": "Product added (#{id}): {title}\n\n💰 Current price: {price:.2f}",
        "view_product": "🔗 View product",
        "delete_product": "🗑 Delete ❌",
        "history_button": "📈 History",
        "list_empty": "You're not tracking any product yet.",
        "list_end": "End of list.",
        "product_line": "#{id} - {title}\n\n💰 Current price: {price:.2f}",
        "untrack_usage": "Usage: /untrack <id>",
        "untrack_invalid_id": "The id must be a number.",
        "untrack_not_found": "Product not found.",
        "untrack_not_found_button": "Product not found or already deleted.",
        "untrack_success": "Product #{id} deleted.",
        "untrack_success_button": "Product #{id} deleted: {title}",
        "price_drop": "Price drop",
        "price_rise": "Price increase",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Something went wrong, try again.",
        "choose_language": "🌐 Choose your language:",
        "language_set": "Language updated: {name}",
        "history_empty": "No price changes so far for {title}.",
        "history_header": "Price history — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Choose a product to see its history:",
    },
    "es": {
        "help": (
            "Hola 👋 Soy tu asistente de seguimiento de precios de Amazon: "
            "vigilo los productos que me indiques y te aviso en cuanto cambie su precio.\n\n"
            "/track <url> - seguir un producto\n"
            "/list - ver tus productos seguidos\n"
            "/untrack <id> - dejar de seguir un producto\n"
            "/history - ver el historial de precios de un producto\n"
            "/language - cambiar de idioma\n\n"
            "/help - mostrar esta ayuda"
        ),
        "menu_track": "🔍 Seguir un producto",
        "menu_list": "📋 Mis productos",
        "menu_help": "❓ Ayuda",
        "menu_language": "🌐 Idioma",
        "menu_history": "📈 Historial",
        "ask_link": "📋 Pega abajo el enlace del producto de Amazon a seguir.",
        "fetching": "Obteniendo el precio...",
        "scrape_failed": "No pude obtener el precio de este producto. Revisa el enlace.",
        "product_added": "Producto añadido (#{id}): {title}\n\n💰 Precio actual: {price:.2f}",
        "view_product": "🔗 Ver producto",
        "delete_product": "🗑 Eliminar ❌",
        "history_button": "📈 Historial",
        "list_empty": "Todavía no sigues ningún producto.",
        "list_end": "Fin de la lista.",
        "product_line": "#{id} - {title}\n\n💰 Precio actual: {price:.2f}",
        "untrack_usage": "Uso: /untrack <id>",
        "untrack_invalid_id": "El id debe ser un número.",
        "untrack_not_found": "Producto no encontrado.",
        "untrack_not_found_button": "Producto no encontrado o ya eliminado.",
        "untrack_success": "Producto #{id} eliminado.",
        "untrack_success_button": "Producto #{id} eliminado: {title}",
        "price_drop": "Bajada de precio",
        "price_rise": "Subida de precio",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Ha ocurrido un error, inténtalo de nuevo.",
        "choose_language": "🌐 Elige tu idioma:",
        "language_set": "Idioma actualizado: {name}",
        "history_empty": "Sin cambios de precio hasta la fecha para {title}.",
        "history_header": "Historial de precios — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Elige un producto para ver su historial:",
    },
    "de": {
        "help": (
            "Hallo 👋 Ich bin dein Amazon-Preisverfolgungs-Assistent: "
            "Ich beobachte die Produkte, die du mir angibst, und benachrichtige dich, "
            "sobald sich der Preis ändert.\n\n"
            "/track <url> - Produkt verfolgen\n"
            "/list - verfolgte Produkte anzeigen\n"
            "/untrack <id> - Produkt nicht mehr verfolgen\n"
            "/history - Preisverlauf eines Produkts ansehen\n"
            "/language - Sprache ändern\n\n"
            "/help - diese Hilfe anzeigen"
        ),
        "menu_track": "🔍 Produkt verfolgen",
        "menu_list": "📋 Meine Produkte",
        "menu_help": "❓ Hilfe",
        "menu_language": "🌐 Sprache",
        "menu_history": "📈 Verlauf",
        "ask_link": "📋 Füge unten den Amazon-Produktlink ein, den du verfolgen möchtest.",
        "fetching": "Preis wird abgerufen...",
        "scrape_failed": "Ich konnte den Preis für dieses Produkt nicht abrufen. Überprüfe den Link.",
        "product_added": "Produkt hinzugefügt (#{id}): {title}\n\n💰 Aktueller Preis: {price:.2f}",
        "view_product": "🔗 Produkt ansehen",
        "delete_product": "🗑 Löschen ❌",
        "history_button": "📈 Verlauf",
        "list_empty": "Du verfolgst noch kein Produkt.",
        "list_end": "Ende der Liste.",
        "product_line": "#{id} - {title}\n\n💰 Aktueller Preis: {price:.2f}",
        "untrack_usage": "Verwendung: /untrack <id>",
        "untrack_invalid_id": "Die ID muss eine Zahl sein.",
        "untrack_not_found": "Produkt nicht gefunden.",
        "untrack_not_found_button": "Produkt nicht gefunden oder bereits gelöscht.",
        "untrack_success": "Produkt #{id} gelöscht.",
        "untrack_success_button": "Produkt #{id} gelöscht: {title}",
        "price_drop": "Preissenkung",
        "price_rise": "Preiserhöhung",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Ein Fehler ist aufgetreten, versuch es erneut.",
        "choose_language": "🌐 Wähle deine Sprache:",
        "language_set": "Sprache aktualisiert: {name}",
        "history_empty": "Bisher keine Preisänderung für {title}.",
        "history_header": "Preisverlauf — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Wähle ein Produkt, um den Verlauf zu sehen:",
    },
}


def t(key: str, lang: str, **kwargs) -> str:
    lang = lang if lang in TRANSLATIONS else DEFAULT_LANG
    template = TRANSLATIONS[lang].get(key, TRANSLATIONS[DEFAULT_LANG][key])
    return template.format(**kwargs) if kwargs else template

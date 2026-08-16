DEFAULT_LANG = "fr"

LANGUAGE_NAMES = {
    "fr": "Français 🇫🇷",
    "en": "English 🇬🇧",
    "es": "Español 🇪🇸",
    "de": "Deutsch 🇩🇪",
    "pt": "Português 🇵🇹",
    "ru": "Русский 🇷🇺",
}

TRANSLATIONS = {
    "fr": {
        "help": (
            "Salut 👋 Je suis ton assistant de suivi de prix Amazon : "
            "je surveille les produits que tu m'indiques.\n\n"
            "Je vérifie les prix toutes les ⏱️ <b>3h</b> et je te préviens dès qu'ils changent, "
            "en gardant un historique fiable de chaque changement.\n\n"
            "/track &lt;url&gt; - suivre un produit\n"
            "/list - voir mes produits suivis\n"
            "/untrack &lt;id&gt; - arrêter de suivre un produit\n"
            "/history - consulter l'historique d'un produit\n"
            "/language - changer de langue\n"
            "/contact - me contacter\n\n"
            "/help - afficher cette aide"
        ),
        "menu_track": "🔍 Suivre un produit",
        "menu_list": "📋 Mes produits",
        "menu_help": "❓ Aide",
        "menu_language": "🌐 Langue",
        "menu_history": "📈 Historique",
        "menu_contact": "📞 Contact",
        "ask_link": "📋 Colle le lien du produit Amazon à suivre ci-dessous.",
        "fetching": "Récupération du prix en cours...",
        "scrape_failed": "Je n'ai pas réussi à récupérer le prix de ce produit. Vérifie le lien.",
        "product_added": "Produit ajouté (#{id}) : {title}\n\n💰 Prix actuel : {price:.2f}",
        "view_product": "🔗 Voir sur Amazon",
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
        "price_drop": "📉 Baisse de prix",
        "price_rise": "📈 Hausse de prix",
        "price_alert": "{direction} ! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Une erreur est survenue, réessaie.",
        "choose_language": "🌐 Choisis ta langue :",
        "language_set": "Langue mise à jour : {name}",
        "history_empty": "Aucun changement de prix à ce jour pour {title}.",
        "history_header": "Historique des prix — {title} :",
        "history_line": "{date} : {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Choisis un produit pour voir son historique :",
        "contact_text": "📞 Contact\n\nGitHub : github.com/choncotm\nSite web : choncotm.com\nEmail : choncotmexe@outlook.com",
    },
    "en": {
        "help": (
            "Hi 👋 I'm your Amazon price-tracking assistant: "
            "I watch the products you give me.\n\n"
            "I check prices every ⏱️ <b>3 hours</b> and notify you whenever they change, "
            "keeping a reliable history of every change.\n\n"
            "/track &lt;url&gt; - track a product\n"
            "/list - view your tracked products\n"
            "/untrack &lt;id&gt; - stop tracking a product\n"
            "/history - view a product's price history\n"
            "/language - change language\n"
            "/contact - contact me\n\n"
            "/help - show this help"
        ),
        "menu_track": "🔍 Track a product",
        "menu_list": "📋 My products",
        "menu_help": "❓ Help",
        "menu_language": "🌐 Language",
        "menu_history": "📈 History",
        "menu_contact": "📞 Contact",
        "ask_link": "📋 Paste the Amazon product link to track below.",
        "fetching": "Fetching the price...",
        "scrape_failed": "I couldn't fetch the price for this product. Check the link.",
        "product_added": "Product added (#{id}): {title}\n\n💰 Current price: {price:.2f}",
        "view_product": "🔗 View on Amazon",
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
        "price_drop": "📉 Price drop",
        "price_rise": "📈 Price increase",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Something went wrong, try again.",
        "choose_language": "🌐 Choose your language:",
        "language_set": "Language updated: {name}",
        "history_empty": "No price changes so far for {title}.",
        "history_header": "Price history — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Choose a product to see its history:",
        "contact_text": "📞 Contact\n\nGitHub: github.com/choncotm\nWebsite: choncotm.com\nEmail: choncotmexe@outlook.com",
    },
    "es": {
        "help": (
            "Hola 👋 Soy tu asistente de seguimiento de precios de Amazon: "
            "vigilo los productos que me indiques.\n\n"
            "Reviso los precios cada ⏱️ <b>3 horas</b> y te aviso en cuanto cambien, "
            "manteniendo un historial fiable de cada cambio.\n\n"
            "/track &lt;url&gt; - seguir un producto\n"
            "/list - ver tus productos seguidos\n"
            "/untrack &lt;id&gt; - dejar de seguir un producto\n"
            "/history - ver el historial de precios de un producto\n"
            "/language - cambiar de idioma\n"
            "/contact - contactarme\n\n"
            "/help - mostrar esta ayuda"
        ),
        "menu_track": "🔍 Seguir un producto",
        "menu_list": "📋 Mis productos",
        "menu_help": "❓ Ayuda",
        "menu_language": "🌐 Idioma",
        "menu_history": "📈 Historial",
        "menu_contact": "📞 Contacto",
        "ask_link": "📋 Pega abajo el enlace del producto de Amazon a seguir.",
        "fetching": "Obteniendo el precio...",
        "scrape_failed": "No pude obtener el precio de este producto. Revisa el enlace.",
        "product_added": "Producto añadido (#{id}): {title}\n\n💰 Precio actual: {price:.2f}",
        "view_product": "🔗 Ver en Amazon",
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
        "price_drop": "📉 Bajada de precio",
        "price_rise": "📈 Subida de precio",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Ha ocurrido un error, inténtalo de nuevo.",
        "choose_language": "🌐 Elige tu idioma:",
        "language_set": "Idioma actualizado: {name}",
        "history_empty": "Sin cambios de precio hasta la fecha para {title}.",
        "history_header": "Historial de precios — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Elige un producto para ver su historial:",
        "contact_text": "📞 Contacto\n\nGitHub: github.com/choncotm\nSitio web: choncotm.com\nCorreo: choncotmexe@outlook.com",
    },
    "de": {
        "help": (
            "Hallo 👋 Ich bin dein Amazon-Preisverfolgungs-Assistent: "
            "Ich beobachte die Produkte, die du mir angibst.\n\n"
            "Ich überprüfe die Preise alle ⏱️ <b>3 Stunden</b> und benachrichtige dich, sobald sie "
            "sich ändern, und führe dabei einen zuverlässigen Verlauf jeder Änderung.\n\n"
            "/track &lt;url&gt; - Produkt verfolgen\n"
            "/list - verfolgte Produkte anzeigen\n"
            "/untrack &lt;id&gt; - Produkt nicht mehr verfolgen\n"
            "/history - Preisverlauf eines Produkts ansehen\n"
            "/language - Sprache ändern\n"
            "/contact - Kontakt zu mir\n\n"
            "/help - diese Hilfe anzeigen"
        ),
        "menu_track": "🔍 Produkt verfolgen",
        "menu_list": "📋 Meine Produkte",
        "menu_help": "❓ Hilfe",
        "menu_language": "🌐 Sprache",
        "menu_history": "📈 Verlauf",
        "menu_contact": "📞 Kontakt",
        "ask_link": "📋 Füge unten den Amazon-Produktlink ein, den du verfolgen möchtest.",
        "fetching": "Preis wird abgerufen...",
        "scrape_failed": "Ich konnte den Preis für dieses Produkt nicht abrufen. Überprüfe den Link.",
        "product_added": "Produkt hinzugefügt (#{id}): {title}\n\n💰 Aktueller Preis: {price:.2f}",
        "view_product": "🔗 Auf Amazon ansehen",
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
        "price_drop": "📉 Preissenkung",
        "price_rise": "📈 Preiserhöhung",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Ein Fehler ist aufgetreten, versuch es erneut.",
        "choose_language": "🌐 Wähle deine Sprache:",
        "language_set": "Sprache aktualisiert: {name}",
        "history_empty": "Bisher keine Preisänderung für {title}.",
        "history_header": "Preisverlauf — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Wähle ein Produkt, um den Verlauf zu sehen:",
        "contact_text": "📞 Kontakt\n\nGitHub: github.com/choncotm\nWebsite: choncotm.com\nE-Mail: choncotmexe@outlook.com",
    },
    "pt": {
        "help": (
            "Olá 👋 Sou o teu assistente de monitorização de preços da Amazon: "
            "vigio os produtos que me indicares.\n\n"
            "Verifico os preços a cada ⏱️ <b>3 horas</b> e aviso-te sempre que mudarem, "
            "mantendo um histórico fiável de cada alteração.\n\n"
            "/track &lt;url&gt; - seguir um produto\n"
            "/list - ver os produtos que segues\n"
            "/untrack &lt;id&gt; - deixar de seguir um produto\n"
            "/history - ver o histórico de preços de um produto\n"
            "/language - mudar de idioma\n"
            "/contact - contactar-me\n\n"
            "/help - mostrar esta ajuda"
        ),
        "menu_track": "🔍 Seguir um produto",
        "menu_list": "📋 Os meus produtos",
        "menu_help": "❓ Ajuda",
        "menu_language": "🌐 Idioma",
        "menu_history": "📈 Histórico",
        "menu_contact": "📞 Contacto",
        "ask_link": "📋 Cola abaixo o link do produto da Amazon a seguir.",
        "fetching": "A obter o preço...",
        "scrape_failed": "Não consegui obter o preço deste produto. Verifica o link.",
        "product_added": "Produto adicionado (#{id}): {title}\n\n💰 Preço atual: {price:.2f}",
        "view_product": "🔗 Ver na Amazon",
        "delete_product": "🗑 Eliminar ❌",
        "history_button": "📈 Histórico",
        "list_empty": "Ainda não segues nenhum produto.",
        "list_end": "Fim da lista.",
        "product_line": "#{id} - {title}\n\n💰 Preço atual: {price:.2f}",
        "untrack_usage": "Uso: /untrack <id>",
        "untrack_invalid_id": "O id deve ser um número.",
        "untrack_not_found": "Produto não encontrado.",
        "untrack_not_found_button": "Produto não encontrado ou já eliminado.",
        "untrack_success": "Produto #{id} eliminado.",
        "untrack_success_button": "Produto #{id} eliminado: {title}",
        "price_drop": "📉 Descida de preço",
        "price_rise": "📈 Subida de preço",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Ocorreu um erro, tenta novamente.",
        "choose_language": "🌐 Escolhe o teu idioma:",
        "language_set": "Idioma atualizado: {name}",
        "history_empty": "Ainda não há alterações de preço para {title}.",
        "history_header": "Histórico de preços — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Escolhe um produto para ver o histórico:",
        "contact_text": "📞 Contacto\n\nGitHub: github.com/choncotm\nSite: choncotm.com\nEmail: choncotmexe@outlook.com",
    },
    "ru": {
        "help": (
            "Привет 👋 Я твой помощник по отслеживанию цен на Amazon: "
            "слежу за товарами, которые ты укажешь.\n\n"
            "Проверяю цены каждые ⏱️ <b>3 часа</b> и сообщаю, как только они изменятся, "
            "ведя надёжную историю каждого изменения.\n\n"
            "/track &lt;url&gt; - отслеживать товар\n"
            "/list - показать отслеживаемые товары\n"
            "/untrack &lt;id&gt; - перестать отслеживать товар\n"
            "/history - посмотреть историю цен товара\n"
            "/language - сменить язык\n"
            "/contact - связаться со мной\n\n"
            "/help - показать эту справку"
        ),
        "menu_track": "🔍 Отслеживать товар",
        "menu_list": "📋 Мои товары",
        "menu_help": "❓ Помощь",
        "menu_language": "🌐 Язык",
        "menu_history": "📈 История",
        "menu_contact": "📞 Контакты",
        "ask_link": "📋 Вставь ссылку на товар Amazon, который нужно отслеживать.",
        "fetching": "Получаю цену...",
        "scrape_failed": "Не удалось получить цену этого товара. Проверь ссылку.",
        "product_added": "Товар добавлен (#{id}): {title}\n\n💰 Текущая цена: {price:.2f}",
        "view_product": "🔗 Смотреть на Amazon",
        "delete_product": "🗑 Удалить ❌",
        "history_button": "📈 История",
        "list_empty": "Ты пока не отслеживаешь ни одного товара.",
        "list_end": "Конец списка.",
        "product_line": "#{id} - {title}\n\n💰 Текущая цена: {price:.2f}",
        "untrack_usage": "Использование: /untrack <id>",
        "untrack_invalid_id": "ID должен быть числом.",
        "untrack_not_found": "Товар не найден.",
        "untrack_not_found_button": "Товар не найден или уже удалён.",
        "untrack_success": "Товар #{id} удалён.",
        "untrack_success_button": "Товар #{id} удалён: {title}",
        "price_drop": "📉 Снижение цены",
        "price_rise": "📈 Повышение цены",
        "price_alert": "{direction}! {title}\n{old_price:.2f} -> {new_price:.2f}",
        "error": "Произошла ошибка, попробуй ещё раз.",
        "choose_language": "🌐 Выбери язык:",
        "language_set": "Язык обновлён: {name}",
        "history_empty": "Пока нет изменений цены для {title}.",
        "history_header": "История цен — {title}:",
        "history_line": "{date}: {sign} {old_price:.2f} -> {new_price:.2f}",
        "choose_product_history": "📈 Выбери товар, чтобы посмотреть историю:",
        "contact_text": "📞 Контакты\n\nGitHub: github.com/choncotm\nСайт: choncotm.com\nEmail: choncotmexe@outlook.com",
    },
}


def t(key: str, lang: str, **kwargs) -> str:
    lang = lang if lang in TRANSLATIONS else DEFAULT_LANG
    template = TRANSLATIONS[lang].get(key, TRANSLATIONS[DEFAULT_LANG][key])
    return template.format(**kwargs) if kwargs else template

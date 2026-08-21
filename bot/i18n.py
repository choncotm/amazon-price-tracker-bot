DEFAULT_LANG = "en"

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
            "Salut 👋 Je suis ton assistant de suivi de prix Amazon, le plus réactif du "
            "marché. Jamais un bon plan raté.\n\n"
            "👉 <b>Colle un lien Amazon ici</b>, ou clique sur \"suivre un produit\" pour "
            "démarrer.\n\n"
            "⏱️ Surveillance 24h/24\n"
            "🔔 Alerte instantanée au moindre changement de prix\n"
            "📊 Historique fiable de chaque variation, pour repérer les vraies promos"
        ),
        "menu_track": "🔍 Suivre un produit",
        "menu_list": "📋 Mes produits",
        "back_button": "🔙 Retour",
        "menu_language": "🌐 Langue",
        "menu_history": "📈 Historique",
        "menu_webapp": "🖥️ Gérer sur le web",
        "menu_howitworks": "❓ Comment ça marche",
        "menu_share": "📤 Partager",
        "menu_privacy": "🔒 Confidentialité",
        "menu_contact": "📬 Contact",
        "contact_message": "Retrouve-moi ici :\n\n📧 {email}",
        "contact_website_button": "🌐 Site web",
        "contact_github_button": "💻 GitHub",
        "ask_link": "📋 Colle le lien du produit Amazon à suivre ci-dessous.",
        "fetching": "Récupération du prix en cours...",
        "scrape_failed": "Je n'ai pas réussi à récupérer le prix de ce produit. Vérifie le lien.",
        "product_added": "Produit ajouté (#{id}) : {title}\n\n💰 Prix actuel : {price:.2f}",
        "view_product": "🔗 Voir sur Amazon",
        "delete_product": "❌ Supprimer",
        "history_button": "📈 Historique",
        "list_empty": "Tu ne suis aucun produit pour l'instant.",
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
        "limit_reached": (
            "⚠️ Limite atteinte : {limit}/{limit} produits trackés.\n\n"
            "Pour tracker plus de produits, invite tes amis 👇\n\n"
            "🔗 Partage ton lien : {link}\n\n"
            "👥 1 invité : 10 produits\n"
            "👥 3 invités : 50 produits\n"
            "👥 10 invités : illimité ♾️"
        ),
        "share_message": (
            "🤖 Voici ton lien de parrainage :\n\n{link}\n\n"
            "👥 Tu as parrainé {count} ami(s).\n\n"
            "🎁 1 invité : 10 produits suivis\n"
            "🎁 3 invités : 50 produits suivis\n"
            "🎁 10 invités : suivi illimité ♾️\n\n"
            "Appuie longuement sur le lien pour le copier, ou utilise le bouton ci-dessous "
            "pour le partager directement."
        ),
        "share_open_button": "📤 Partager directement",
        "share_caption": "Suis les prix Amazon avec ce bot 🤖",
    },
    "en": {
        "help": (
            "Hi 👋 I'm your Amazon price-tracking assistant, the most responsive on the "
            "market. Never miss a good deal again.\n\n"
            "👉 <b>Paste an Amazon link here</b>, or tap \"track a product\" to get "
            "started.\n\n"
            "⏱️ 24/7 monitoring\n"
            "🔔 Instant alert on the smallest price change\n"
            "📊 Reliable history of every variation, to spot the real deals"
        ),
        "menu_track": "🔍 Track a product",
        "menu_list": "📋 My products",
        "back_button": "🔙 Back",
        "menu_language": "🌐 Language",
        "menu_history": "📈 History",
        "menu_webapp": "🖥️ Manage on the web",
        "menu_howitworks": "❓ How it works",
        "menu_share": "📤 Share",
        "menu_privacy": "🔒 Privacy",
        "menu_contact": "📬 Contact",
        "contact_message": "Find me here:\n\n📧 {email}",
        "contact_website_button": "🌐 Website",
        "contact_github_button": "💻 GitHub",
        "ask_link": "📋 Paste the Amazon product link to track below.",
        "fetching": "Fetching the price...",
        "scrape_failed": "I couldn't fetch the price for this product. Check the link.",
        "product_added": "Product added (#{id}): {title}\n\n💰 Current price: {price:.2f}",
        "view_product": "🔗 View on Amazon",
        "delete_product": "❌ Delete",
        "history_button": "📈 History",
        "list_empty": "You're not tracking any product yet.",
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
        "limit_reached": (
            "⚠️ Limit reached: {limit}/{limit} products tracked.\n\n"
            "To track more products, invite your friends 👇\n\n"
            "🔗 Share your link: {link}\n\n"
            "👥 1 invite: 10 products\n"
            "👥 3 invites: 50 products\n"
            "👥 10 invites: unlimited ♾️"
        ),
        "share_message": (
            "🤖 Here is your referral link:\n\n{link}\n\n"
            "👥 You've invited {count} friend(s).\n\n"
            "🎁 1 invite: 10 tracked products\n"
            "🎁 3 invites: 50 tracked products\n"
            "🎁 10 invites: unlimited tracking ♾️\n\n"
            "Press and hold the link to copy it, or use the button below to share it "
            "directly."
        ),
        "share_open_button": "📤 Share directly",
        "share_caption": "Track Amazon prices with this bot 🤖",
    },
    "es": {
        "help": (
            "Hola 👋 Soy tu asistente de seguimiento de precios de Amazon, el más rápido "
            "del mercado. Nunca más te pierdas una buena oferta.\n\n"
            "👉 <b>Pega un enlace de Amazon aquí</b>, o toca \"seguir un producto\" para "
            "empezar.\n\n"
            "⏱️ Vigilancia 24/7\n"
            "🔔 Alerta instantánea ante el más mínimo cambio de precio\n"
            "📊 Historial fiable de cada variación, para detectar las ofertas reales"
        ),
        "menu_track": "🔍 Seguir un producto",
        "menu_list": "📋 Mis productos",
        "back_button": "🔙 Volver",
        "menu_language": "🌐 Idioma",
        "menu_history": "📈 Historial",
        "menu_webapp": "🖥️ Gestionar en la web",
        "menu_howitworks": "❓ Cómo funciona",
        "menu_share": "📤 Compartir",
        "menu_privacy": "🔒 Privacidad",
        "menu_contact": "📬 Contacto",
        "contact_message": "Encuéntrame aquí:\n\n📧 {email}",
        "contact_website_button": "🌐 Sitio web",
        "contact_github_button": "💻 GitHub",
        "ask_link": "📋 Pega abajo el enlace del producto de Amazon a seguir.",
        "fetching": "Obteniendo el precio...",
        "scrape_failed": "No pude obtener el precio de este producto. Revisa el enlace.",
        "product_added": "Producto añadido (#{id}): {title}\n\n💰 Precio actual: {price:.2f}",
        "view_product": "🔗 Ver en Amazon",
        "delete_product": "❌ Eliminar",
        "history_button": "📈 Historial",
        "list_empty": "Todavía no sigues ningún producto.",
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
        "limit_reached": (
            "⚠️ Límite alcanzado: {limit}/{limit} productos seguidos.\n\n"
            "Para seguir más productos, invita a tus amigos 👇\n\n"
            "🔗 Comparte tu enlace: {link}\n\n"
            "👥 1 invitado: 10 productos\n"
            "👥 3 invitados: 50 productos\n"
            "👥 10 invitados: ilimitado ♾️"
        ),
        "share_message": (
            "🤖 Aquí tienes tu enlace de referidos:\n\n{link}\n\n"
            "👥 Has invitado a {count} amigo(s).\n\n"
            "🎁 1 invitado: 10 productos seguidos\n"
            "🎁 3 invitados: 50 productos seguidos\n"
            "🎁 10 invitados: seguimiento ilimitado ♾️\n\n"
            "Mantén pulsado el enlace para copiarlo, o usa el botón de abajo para "
            "compartirlo directamente."
        ),
        "share_open_button": "📤 Compartir directamente",
        "share_caption": "Sigue los precios de Amazon con este bot 🤖",
    },
    "de": {
        "help": (
            "Hallo 👋 Ich bin dein Amazon-Preisverfolgungs-Assistent, der "
            "reaktionsschnellste auf dem Markt. Verpasse nie wieder ein gutes Angebot.\n\n"
            "👉 <b>Füge hier einen Amazon-Link ein</b>, oder tippe auf \"Produkt "
            "verfolgen\", um zu starten.\n\n"
            "⏱️ Überwachung rund um die Uhr\n"
            "🔔 Sofortige Benachrichtigung bei jeder Preisänderung\n"
            "📊 Zuverlässiger Verlauf jeder Änderung, um echte Angebote zu erkennen"
        ),
        "menu_track": "🔍 Produkt verfolgen",
        "menu_list": "📋 Meine Produkte",
        "back_button": "🔙 Zurück",
        "menu_language": "🌐 Sprache",
        "menu_history": "📈 Verlauf",
        "menu_webapp": "🖥️ Im Web verwalten",
        "menu_howitworks": "❓ So funktioniert's",
        "menu_share": "📤 Teilen",
        "menu_privacy": "🔒 Datenschutz",
        "menu_contact": "📬 Kontakt",
        "contact_message": "Hier findest du mich:\n\n📧 {email}",
        "contact_website_button": "🌐 Website",
        "contact_github_button": "💻 GitHub",
        "ask_link": "📋 Füge unten den Amazon-Produktlink ein, den du verfolgen möchtest.",
        "fetching": "Preis wird abgerufen...",
        "scrape_failed": "Ich konnte den Preis für dieses Produkt nicht abrufen. Überprüfe den Link.",
        "product_added": "Produkt hinzugefügt (#{id}): {title}\n\n💰 Aktueller Preis: {price:.2f}",
        "view_product": "🔗 Auf Amazon ansehen",
        "delete_product": "❌ Löschen",
        "history_button": "📈 Verlauf",
        "list_empty": "Du verfolgst noch kein Produkt.",
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
        "limit_reached": (
            "⚠️ Limit erreicht: {limit}/{limit} Produkte verfolgt.\n\n"
            "Um mehr Produkte zu verfolgen, lade deine Freunde ein 👇\n\n"
            "🔗 Teile deinen Link: {link}\n\n"
            "👥 1 Einladung: 10 Produkte\n"
            "👥 3 Einladungen: 50 Produkte\n"
            "👥 10 Einladungen: unbegrenzt ♾️"
        ),
        "share_message": (
            "🤖 Hier ist dein Empfehlungslink:\n\n{link}\n\n"
            "👥 Du hast {count} Freund(e) eingeladen.\n\n"
            "🎁 1 Einladung: 10 verfolgte Produkte\n"
            "🎁 3 Einladungen: 50 verfolgte Produkte\n"
            "🎁 10 Einladungen: unbegrenztes Tracking ♾️\n\n"
            "Halte den Link gedrückt, um ihn zu kopieren, oder nutze den Button unten, um "
            "ihn direkt zu teilen."
        ),
        "share_open_button": "📤 Direkt teilen",
        "share_caption": "Verfolge Amazon-Preise mit diesem Bot 🤖",
    },
    "pt": {
        "help": (
            "Olá 👋 Sou o teu assistente de monitorização de preços da Amazon, o mais "
            "rápido do mercado. Nunca mais percas uma boa promoção.\n\n"
            "👉 <b>Cola um link da Amazon aqui</b>, ou toca em \"seguir um produto\" para "
            "começar.\n\n"
            "⏱️ Monitorização 24h/24\n"
            "🔔 Alerta instantâneo à mínima alteração de preço\n"
            "📊 Histórico fiável de cada variação, para identificar as promoções reais"
        ),
        "menu_track": "🔍 Seguir um produto",
        "menu_list": "📋 Os meus produtos",
        "back_button": "🔙 Voltar",
        "menu_language": "🌐 Idioma",
        "menu_history": "📈 Histórico",
        "menu_webapp": "🖥️ Gerir na web",
        "menu_howitworks": "❓ Como funciona",
        "menu_share": "📤 Partilhar",
        "menu_privacy": "🔒 Privacidade",
        "menu_contact": "📬 Contacto",
        "contact_message": "Encontra-me aqui:\n\n📧 {email}",
        "contact_website_button": "🌐 Site",
        "contact_github_button": "💻 GitHub",
        "ask_link": "📋 Cola abaixo o link do produto da Amazon a seguir.",
        "fetching": "A obter o preço...",
        "scrape_failed": "Não consegui obter o preço deste produto. Verifica o link.",
        "product_added": "Produto adicionado (#{id}): {title}\n\n💰 Preço atual: {price:.2f}",
        "view_product": "🔗 Ver na Amazon",
        "delete_product": "❌ Eliminar",
        "history_button": "📈 Histórico",
        "list_empty": "Ainda não segues nenhum produto.",
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
        "limit_reached": (
            "⚠️ Limite atingido: {limit}/{limit} produtos monitorizados.\n\n"
            "Para monitorizar mais produtos, convida os teus amigos 👇\n\n"
            "🔗 Partilha o teu link: {link}\n\n"
            "👥 1 convidado: 10 produtos\n"
            "👥 3 convidados: 50 produtos\n"
            "👥 10 convidados: ilimitado ♾️"
        ),
        "share_message": (
            "🤖 Aqui está o teu link de referência:\n\n{link}\n\n"
            "👥 Convidaste {count} amigo(s).\n\n"
            "🎁 1 convidado: 10 produtos monitorizados\n"
            "🎁 3 convidados: 50 produtos monitorizados\n"
            "🎁 10 convidados: monitorização ilimitada ♾️\n\n"
            "Mantém premido o link para o copiar, ou usa o botão abaixo para o partilhar "
            "diretamente."
        ),
        "share_open_button": "📤 Partilhar diretamente",
        "share_caption": "Acompanha os preços da Amazon com este bot 🤖",
    },
    "ru": {
        "help": (
            "Привет 👋 Я твой помощник по отслеживанию цен на Amazon, самый быстрый на "
            "рынке. Больше никогда не упустишь выгодное предложение.\n\n"
            "👉 <b>Вставь сюда ссылку Amazon</b> или нажми «отслеживать товар», чтобы "
            "начать.\n\n"
            "⏱️ Отслеживание 24/7\n"
            "🔔 Мгновенное уведомление при малейшем изменении цены\n"
            "📊 Надёжная история каждого изменения, чтобы находить настоящие скидки"
        ),
        "menu_track": "🔍 Отслеживать товар",
        "menu_list": "📋 Мои товары",
        "back_button": "🔙 Назад",
        "menu_language": "🌐 Язык",
        "menu_history": "📈 История",
        "menu_webapp": "🖥️ Управлять на сайте",
        "menu_howitworks": "❓ Как это работает",
        "menu_share": "📤 Поделиться",
        "menu_privacy": "🔒 Конфиденциальность",
        "menu_contact": "📬 Контакты",
        "contact_message": "Найди меня здесь:\n\n📧 {email}",
        "contact_website_button": "🌐 Сайт",
        "contact_github_button": "💻 GitHub",
        "ask_link": "📋 Вставь ссылку на товар Amazon, который нужно отслеживать.",
        "fetching": "Получаю цену...",
        "scrape_failed": "Не удалось получить цену этого товара. Проверь ссылку.",
        "product_added": "Товар добавлен (#{id}): {title}\n\n💰 Текущая цена: {price:.2f}",
        "view_product": "🔗 Смотреть на Amazon",
        "delete_product": "❌ Удалить",
        "history_button": "📈 История",
        "list_empty": "Ты пока не отслеживаешь ни одного товара.",
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
        "limit_reached": (
            "⚠️ Достигнут лимит: {limit}/{limit} отслеживаемых товаров.\n\n"
            "Чтобы отслеживать больше товаров, пригласи друзей 👇\n\n"
            "🔗 Поделись своей ссылкой: {link}\n\n"
            "👥 1 приглашение: 10 товаров\n"
            "👥 3 приглашения: 50 товаров\n"
            "👥 10 приглашений: без ограничений ♾️"
        ),
        "share_message": (
            "🤖 Вот твоя реферальная ссылка:\n\n{link}\n\n"
            "👥 Ты пригласил(а) {count} друзей.\n\n"
            "🎁 1 приглашение: 10 отслеживаемых товаров\n"
            "🎁 3 приглашения: 50 отслеживаемых товаров\n"
            "🎁 10 приглашений: безлимитное отслеживание ♾️\n\n"
            "Зажми ссылку, чтобы скопировать её, или используй кнопку ниже, чтобы "
            "поделиться напрямую."
        ),
        "share_open_button": "📤 Поделиться напрямую",
        "share_caption": "Отслеживай цены на Amazon с этим ботом 🤖",
    },
}


def t(key: str, lang: str, **kwargs) -> str:
    lang = lang if lang in TRANSLATIONS else DEFAULT_LANG
    template = TRANSLATIONS[lang].get(key, TRANSLATIONS[DEFAULT_LANG][key])
    return template.format(**kwargs) if kwargs else template

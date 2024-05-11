from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class MenuItem:
    name: str
    photo: Path
    text: str


@dataclass
class ArchType:
    main_text: str
    late_thanks_text: str

    def __post_init__(self):
        self.late_thanks_text += '\n@Arhetype_Mentor'


@dataclass
class CheckList:
    name: str
    file: Path | str
    text: Optional[str] = None


info_menu_items = \
    [
        MenuItem("🤔Что такое Архетипы?", Path("photos/arhtypes_is.png"),
                 "🔑Архетипы - это определенные энергии в коллективном бессознательном; это сценарии подсознания, которые движут нами каждую секунду🔥"),
        MenuItem("😱Факты об Архетипах", Path("photos/facts_about_arhtypes.png"),
                 "3 ВАЖНЫХ ФАКТА об Архетипах🔥\n\n1️⃣ - Некоторые ученые считают, что в мифах Древней Греции описаны Архетипы. Ведь:\n- Архетипы обладают огромной\nвластью над жизнью простых людей.\nОни ею управляют.\n- Они бессмертны.\n- Они ведут себя как люди.\n\n2️⃣ - Архетипы дуальны: имеют Тень (слабые стороны) и Свет (сильные стороны). Свет энергию даёт, Тень забирает. Архетипы проявляются в нашей жизни каждую секунду, им все равно как проигрываться (через Тень или Свет), а вот нам нет — ведь от этого зависит счастливы мы\nили страдаем.\n\n3️⃣ - Тень Архетипа можно перевести в Свет, если совершать компенсаторные действия. Для каждого Архетипа они свои."),
        MenuItem("🃏Как вычисляются архетипы?", Path("photos/how_to_count_arh_type.png"),
                 "✒️Архетипы - это универсальные символы и образы, которые представляют основные аспекты человеческой психологии и опыта. Рассчитать архетипы можно путем анализа символов, мифов, легенд, сказок, историй и других культурных произведений.\n👆🏼Существует несколько подходов к определению архетипов, и каждый из них может быть полезным в разных контекстах.\nОдним из таких подходов является метод Карла Юнга, который разработал систему аналитической психологии. Согласно Юнгу, архетипы являются бессознательными содержаниями, которые проявляются в нашей жизни через символы и образы.\n✨Чтобы рассчитать архетипы с помощью метода Юнга, необходимо провести процесс анализа символов, образов и историй. Для этого нужно:\n 1. Выбрать материал для анализа. Это может быть любой культурный материал, например, мифы, сказки, религиозные тексты, литературные произведения, фильмы и т.д.\n 2. Выделить ключевые символы и образы. Это могут быть любые элементы материала, которые вызывают эмоциональную реакцию и имеют значимость для сюжета или темы.\n 3. Определить частоту появления каждого символа и образа. Частота появления поможет определить, какие символы и образы являются наиболее значимыми для данного материала.\n 4. Сравнить результаты с известными архетипами. Существует множество каталогов архетипов, которые могут помочь определить, какие архетипы соответствуют символам и образам, выделенным в материале.\n 5. Интерпретировать результаты. Архетипы могут использоваться для понимания человеческой психологии, культурных трендов и социальных изменений.\n✋🏻Важно понимать, что архетипы не являются жесткими рамками для определения личности или поведения людей. Они скорее представляют собой универсальные образы, которые помогают нам лучше понимать мир и себя в нем.")    ]
arch_types = \
    [
        ArchType(
            "💫Сегодня мы поговорим об архетипе Правителя. И узнаем, какими сильными и слабыми сторонами Вы обладаете, исходя из качеств данного архетипа.\n\n🌙Правитель - это архетип лидера, управляющего и организующего все вокруг себя.\n\nЕсли Вы являетесь представителем этого архетипа, то, вероятно, Вам легко дается принятие решений, установление целей и реализация проектов.\n\nВы можете быть успешным в бизнесе и управлении людьми.",
            "Спасибо, что воспользовались нашей эмодзи методикой самопознания! ✨\n\nЯ надеюсь, что Вы узнали что-то новое о себе, осознали свой потенциал и понимаете, как использовать его для достижения своих целей.\n\n📝Если у Вас есть какие-либо вопросы или Вы хотите обсудить свой архетип Правителя, обращайтесь ко мне в личных сообщениях."),

        ArchType(
            "💫Сегодня мы поговорим о Вашем архетипе шута. И узнаем, какими сильными и слабыми качествами Вы обладаете!\n\nЭтот архетип символизирует юмор, развлечение, игривость и свободу. Давайте узнаем, как этот архетип работает в Вас и как вы можете использовать его для достижения более светлой и радостной жизни.\n\nШут - это архетип, который символизирует игривость, свободу, юмор и развлечение. Люди с этим архетипом, как правило, умеют отвлечься от проблем и наслаждаться моментом.\n\nОни любят прикалываться и шутить, но не забывают про свои обязанности.\nШут может помочь нам посмотреть на вещи с другой стороны и найти в них что-то положительное.",
            "Спасибо за использование моей методики самопознания! 💫\n\nЯ надеюсь, что Вы смогли почувствовать свободу и легкость Шута, и осознали, что жизнь - это игра.\n\n✒️Если у Вас есть какие-либо вопросы по поводу архетипа Шута или Вы хотите обсудить что-то личное, обращайтесь ко мне в личных сообщениях."),

        ArchType(
            "💫Сегодня мы рассмотрим Ваш архетип - славный малый. Этот архетип символизирует духовное богатство, невинность и радость жизни. Давайте выясним, как использовать его для создания яркой и интересной жизни.\n\nСлавный малый - это человек, который не боится показывать свои эмоции и выражать свои желания.\n\nОн верит в чудеса и всегда находит повод для улыбки.\n\nСлавный малый может быть душой компании и дарить окружающим позитивную энергию.",
            "Благодарю Вас за использование моей методики. 💫\n\nСлавный малый - это прекрасный архетип, который помогает находить радость в жизни и не бояться проявлять свои эмоции.\n\nЕсли у Вас будут вопросы по работе с этим архетипом, обращайтесь ко мне в личные сообщения📝"),

        ArchType(
            "💫Сегодня мы изучим Ваш архетип - бунтарь. Бунтарь всегда идет своей дорогой, не признает авторитетов и старается сделать все по-своему.\n\nДавайте разберемся, как этот архетип влияет на вашу жизнь и как использовать его для достижения целей.\n\nБунтарь - это человек, который стремится изменить устоявшийся порядок вещей, не боясь конфликтов и рисков.\n\nОн готов идти на противостояние с обществом и властью, если это необходимо для защиты своих убеждений и интересов.\n\nБунтарь нередко обладает ярким харизматическим лидерством и способен вдохновлять других на перемену.",
            "Спасибо, что воспользовались моей методикой и изучили свой архетип.❤️\n\nБунтарь - это сильный и уверенный в себе архетип, который может помочь вам стать успешным и достичь поставленных целей.\n\n✒️Если у Вас возникнут вопросы по поводу работы с этим архетипом, обращайтесь ко мне в любое время."),

        ArchType(
            '💫Я рада приветствовать Вас здесь. Сегодня мы изучим Ваш архетип Влюбленного/Влюбленной и поймем, как с ним работать для достижения гармонии, удовлетворенности жизнью и полного счастья!\n\nАрхетип "Влюбленная/влюбленный" относится к типу личности, которая ищет идеальную любовь, находит красоту во всем и искренне верит в романтику.\n\nОни могут быть очень чувствительными и эмоциональными, а также могут иметь тенденцию к идеализации своих отношений.\n\nЛюди с этим архетипом могут часто переживать из-за любовных дел и быть склонными к поиску новых впечатлений и приключений в своих отношениях.\n\nОни обладают тонкой интуицией и пониманием чувств других людей, что позволяет им легко создавать глубокие и крепкие отношения.',
            'Спасибо, что узнали свой архетип Влюбленного/Влюбленной. 🤍\n\nЯ надеюсь, что это поможет Вам лучше понять себя и свои чувства.\n\nЕсли у Вас есть какие-либо вопросы или нужна помощь, обращайтесь к нам в любое время.✒️'),

        ArchType(
            "💫Сегодня мы изучим Ваш архетип Исследователя/Исследовательницы и поймем, как с ним работать для достижения гармонии, удовлетворенности жизнью и полного счастья!\n\nАрхетип исследователя или исследовательницы относится к категории архетипов в психологии, который представляет собой стремление к знаниям и пониманию окружающего мира\n\nОн олицетворяет желание искать новые знания, глубоко изучать тему, задавать вопросы и искать ответы.\n\nЛюди, которые обладают этим архетипом, обычно высоко ценят знания и образование, они часто изучают науку, историю, философию и другие области знаний.\n\nЛюди с архетипом исследователя могут быть очень целеустремленными и настойчивыми в своих поисках знаний и понимания.\nОни могут быть независимыми мыслителями, которые не боятся ставить под сомнение устоявшиеся идеи и искать новые подходы к решению проблем.\n✨Вместе с тем, они могут также быть склонны к изоляции и часто предпочитают работать самостоятельно.",
            "Спасибо, что узнали свой архетип Исследователя/Исследовательницы✨.\nЯ надеюсь, что это поможет Вам лучше понять свой уникальный путь и желание исследовать мир.\n\nЕсли у Вас есть какие-либо вопросы или нужна помощь, обращайтесь к нам в любое время.📝"),

        ArchType(
            "🤍Сегодня мы изучим Ваш архетип Мудреца и поймем, как с ним работать для достижения гармонии, удовлетворенности жизнью и полного счастья!\n\nАрхетип мудрец (или мудреца) ✨- это один из основных архетипов, который представляет собой символ знания, мудрости, интеллекта и образования.\nЭтот архетип может проявляться в разных формах, таких как ученый, учителей, философ или ментор.\n\nЛюди, у которых сильно выражен этот архетип, стремятся к постоянному обучению, получению новых знаний и развитию своих способностей.\nОни обычно ценят интеллектуальные качества, такие как логика, разум, способность к анализу и критическому мышлению.\n\nОднако, когда мудрец принимает слишком доминантную позицию, он может проявляться в виде человека, который теряет связь с эмоциями и реальностью, слишком увлеченный своими знаниями и теориями.\n\nПоэтому, важно находить баланс между мудростью и эмоциональной стабильностью, чтобы использовать знания для блага себе и окружающих людей.",
            "Спасибо, что узнали свой архетип Мудреца. 🤍\nЯ надеюсь, что это поможет Вам лучше понимать свою мудрость и умение советовать другим.\n\nЕсли у Вас есть какие-либо вопросы или нужна помощь, обращайтесь к нам в любое время."),

        ArchType(
            "✨Сегодня мы рассмотрим Ваш архетип Короля/Королевы и поймем, ваши сильные и слабые стороны, а также, подберем стратегию для дальнейшей работы над развитием ваших индивидуальных особенностей характера!\n\nЭтот архетип символизирует лидерство, власть, уверенность и стабильность.\nВы любите быть в центре внимания и принимать важные решения. Вы заботитесь о своей семье, друзьях и близких людях.\n\nВаше влияние распространяется на окружающих, вы являетесь примером для других.",
            "После прохождения теста на определение архетипа, Вы узнали, что ваш архетип Короля/Королевы. Я надеюсь, что этот результат поможет Вам лучше понять себя, свои желания и потребности.\n\n✒️Если у Вас есть какие-либо вопросы или пожелания, не стесняйтесь обращаться ко мне в любое время."),

        ArchType(
            "✋🏻Сегодня мы рассмотрим Ваш архетип Мага/Волшебника.\n\nЭтот архетип символизирует мудрость, знания, творчество и интуицию. Вы любите погружаться в свой внутренний мир, исследовать его и создавать что-то новое.\n\nВы верите в магию и силу мысли. Вы умеете слушать свою интуицию и следовать ей.",
            "✨После прохождения теста на определение архетипа, вы узнали, что ваш архетип Мага/Волшебника.\n\nЯ надеюсь, что этот результат поможет Вам лучше понять себя, свои желания и потребности.\n\n📝Если у Вас есть какие-либо вопросы или пожелания, не стесняйтесь обращаться ко мне в любое время."),

        ArchType(
            "✨Сегодня мы будем изучать архетип Воина. Этот архетип символизирует силу, мужество, целеустремленность и преданность. Готовы узнать больше о себе и своих качествах?\n\nВоин – это архетип, который представляет собой борца, который готов защищать свои идеи, цели и убеждения.\n\nЛюди, чья энергия соответствует архетипу Воина, обладают силой духа, уверенностью в себе и настойчивостью.\n\nОни всегда готовы действовать и достигать поставленных целей, даже если это потребует от них жертв и усилий.",
            "Спасибо за прохождение теста на определение вашего архетипа.❤️\n\nНадеюсь, что теперь Вы лучше понимаете свои качества и сможете использовать их для достижения своих целей.\n\n✒️Если у Вас возникнут какие-либо вопросы или пожелания, обращайтесь ко мне в личные сообщения, Вы также можете поделиться со мной своими наблюдениями и я дам вам консультацию для дальнейшей работы с вашим архетипом"),

        ArchType(
            "😊Сегодня мы изучим Ваш архетип родителя. И разберёмся, какие сильные и слабые стороны есть у этого архетипа, для того, чтоб построить стратегию повеления в этом мире, которая приносила бы только положительные плоды\n\nЭтот архетип символизирует заботу, ответственность, поддержку и любовь к другим.\n\nДавайте узнаем, как этот архетип работает в Вас и как вы можете использовать его для создания более гармоничных отношений с окружающими.\n\nРодитель - это архетип, который символизирует бесконечную любовь и заботу о других людях. Люди с этим архетипом, как правило, заботятся о других, часто забывая о своих собственных нуждах.\nОни всегда готовы помочь другим и уделить свое время и энергию тому, что бы им помочь.\n\nРодительский архетип может проявляться как в личных, так и в профессиональных отношениях.",
            "Спасибо за участие в тестировании! ❤️\n\nНадеюсь, вы смогли больше узнать о своем архетипе родителя и о том, как использовать его для достижения более гармоничных отношений с окружающими.\n\n✍🏻Если у вас есть какие-либо вопросы или нужна помощь в интерпретации результатов, не стесняйтесь обратиться ко мне в личные сообщения."),

        ArchType(
            "❤️Сегодня я расскажу Вам про архетип творца. Этот архетип обладает сильной внутренней мотивацией и стремится к творчеству в различных сферах жизни. Он умеет видеть красоту в мелочах и часто отдаёт предпочтение эстетическому в жизни. Если Вы готовы узнать больше о себе и своих потребностях, то давайте начнём!👇🏽\n\nАрхетип творца – это человек, который наслаждается творческим процессом, стимулируется своим внутренним миром и стремится выразить свою индивидуальность во всём, что делает.\n\nОн обладает неповторимым взглядом на мир и умеет видеть красоту в мелочах.\nТворец может быть художником, писателем, музыкантом, дизайнером или любым другим творческим человеком.\n\nГлавное, что объединяет их всех – это стремление к самореализации и креативному процессу.",
            "Благодарю Вас за прохождение теста на определение вашего архетипа. 🌙\n\nЕсли у Вас возникли какие-либо вопросы или хотите поделиться своими впечатлениями, пожалуйста, обращайтесь ко мне в любое время!\n\nЯ надеюсь, что изучение вашего архетипа поможет Вам лучше понять свои потребности и достичь гармонии в жизни.✒️")
    ]


class Texts:
    start_text = '🧿Здравствуйте! Вы попали в бота по Архетипам!\n\nМоя задача — познакомить Вас с вашими Архетипами! Проявляясь в человеке, архетип стимулирует действие определенной модели поведения, повышает восприимчивость психики человека к определенным образам, явлениям и получаемой информации.🔥\n\n🙏Для начала — я предлагаю сделать Вам бесплатный расчет по Архетипам по дате рождения, нажмите на кнопку "Рассчитать свой архетип"'
    info_menu_text = "✨Здесь Вы сможете узнать чуть больше об архетипах, о том, что это такое, интересные факты и как это вычисляется"
    daily_bonus_menu_text = '🔥Здесь Вы сможете получить подарок от нашего бота\nМы можем предложить вам:\nЧек-лист "Ограничивающие убеждения"\nЧек-лист "Ресурсное состояние"\nУзнать архетип дня'
    info_items: dict[str, MenuItem] = {item.name: item for item in info_menu_items}
    arch_types = arch_types
    calculate_arh_type_item = MenuItem("Рассчитать свой архетип", Path("photos/arhtypes_calculate.png"), "Рассчитайте свои Архетипы за 1 минуту\n\nНапишите свою дату рождения⬇️")
    books_recommendation = MenuItem("📚 Подборка книг об архетипах", Path('photos/books_recomendation.JPG'), '🔔1. Материал будет интересен как арт-терапевтам, так и эзотерикам.\nМандала - круг, система, целостность, единство. Организующий принцип мироздания, минерала, живого организма, человека, устройство внутреннего мира и мира внешних проявлений - в основе всех этих разномасштабных явлений лежит Мандала. Понять природу и принцип Мандалы - значит овла­деть ключом к Тайне. О том, что же такое и как это сделать, рассказывает данная книга.\n\n🔔2. В этой книге Мария-Луиза фон Франц, пользуясь собственным опытом аналитика и опытом сотрудничества с Юнгом, раскрывает многие важные аспекты психологического знания и опыта, накопленного в сказках всего мира. Она это делает очень мудро, пользуясь превосходным знанием фольклора. В основном автор обсуждает проблемы, связанные с Теневой стороной жизни человека: как архетип Тени может проявляться у мужчин и у женщин, что говорят сказки о поведении и сознательных...\n\n🔔3. Анима и анимус являются особо важными архетипическими фигурами. Они, с одной стороны, принадлежат индивидуальному сознанию, а с другой - укоренены в коллективном бессознательном, образуя таким образом связь, или мостик, между личным и внеличностным, сознательным и бессознательным.\n\n🔔4. Книга "Эго и архетип" по праву считается юнгианским культурным бесцеллером. В этой книге, Эдингер подробно, просто и ярко описывает процесс индивидуации, движения индивидуального эго к источнику, и те этапы и стадии, которые проходит личность в этом процессе. Отдельного внимания заслуживает психологическое осмысление Эдингером христианского мифа, где в образе Иисуса Эдингер выводит парадигму индвидуирующегося Эго.\n\n🔔5. Джеймс Хиллман прослеживает интеллектуальную историю архетипической психологии и объясняет корневые понятия и метафоры, составляющие ее практическую основу.\n\nАнализируется архетипическая теория в том виде, в каком ее представлял Карл Густав Юнг, а также обсуждаются идеи других исследователей, ставшие вехами на пути последующего формирования и институализации данного психологического направления. Все это позволяет считать данную работу основным вводным курсом в архетипическую психологию.\n\nВ книгу включена подробная библиография работ как самого Хиллмана, так и его коллег.')

    check_lists = [
        CheckList('📝Получить чек-лист "Ограничивающие убеждения"', Path('check-lists/Ограничивающия убеждения.pdf'),
                  '✨Вы когда-нибудь чувствовали, что что-то вас ограничивает, не дает вам раскрыть свой потенциал?\nВозможно, это ограничивающие убеждения, которые препятствуют вам достижению своих целей и мечтаний.\nНо не беда! Мы создали чек-лист, который поможет Вам их идентифицировать и начать работать с ними.\n💫Получите доступ к нашему чек-листу, чтобы начать жить полной жизнью без ограничений!'),
        CheckList('📝Получить чек-лист "Ресурсное состояние"', Path('check-lists/Ресурсное состояние.pdf'),
                  '🤚🏽Вы когда-нибудь ощущали сильный энергетический напряжение или усталость, которые не позволяют сосредоточиться на важных задачах? Чувствовали, что не можете справиться с вызовами, которые бросает перед вами жизнь?\nРесурсное состояние - это именно то, что Вам нужно, чтобы повысить свою продуктивность и эффективность.\nС помощью нашего чек-листа Вы сможете овладеть техниками, которые помогут Вам управлять своей энергией, контролировать свои мысли и эмоции, и находиться в состоянии, где Вы можете полностью раскрыть свой потенциал.\n✒️Не откладывайте это на потом, получите наш чек-лист прямо сейчас и начните жить жизнью, которую вы заслуживаете!')    ]
    dict_check_lists: dict[str, CheckList] = {check_list.name: check_list for check_list in check_lists}

    daily_arch_types = \
        [
            'Архетип Маг✨\n\n🌝Свет: Вы харизматичные, целеустремлённые, энергичные, успешные, амбициозные и уверенные в себе. Вам важно понимать, кто Вы и зачем пришли в наш мир. Обладаете прекрасными коммуникативными способностями, Ваше слово "заряжено" и Вы с легкостью им владеете.\n\n🌚Тень: Нереализованность, дикая неуверенность в себе, проблемы в коммуникации и страх публичных выступлений, негативное мышление. Не знание ни себя, ни своих истинных желаний и как следствие: сбыча каких-то "левых мечт".',
            'Архетип Шут🃏\n\n🌝Свет: Вы непосредственные, открытые миру, легкие в общении. Детское любопытство - Ваша главная черта. Возможно Вы уже сменили не одну работу, ведь Вы не можете продолжать сидеть на том месте, где уже стало скучно, любите создавать что-то новое, делать то, что до Вас никто не делал. Вы – душа компании, именно вы вносите искру и задор в жизни других людей.\n\n🌚Тень: излишняя доверчивость, наивность. Иногда в порыве восторга или вдохновения можете наделать глупостей. Вообще много проблем в вашей жизни происходит из-за вашей импульсивности. Можете слишком серьезно относиться к жизни или к себе, морально загоняя себя в угол и упуская много возможностей.',
            'Архетип Влюбленные❤️\n\n🌝Свет: Вы романтичные, очаровательные, чувственные и искренние!\nКак и все люди с Архетипом Влюбленные – Вы настоящие лапочки, все Вас обожают, и Вы отвечаете людям теплотой. Влюбленные VI - это проводники энергии любви в наш мир. Вы те, кто умеет по-настоящему любить себя и других, строить партнёрские отношения не только в любви, но и в дружбе и в бизнесе.\n\n🌚Тень: холодность, проблемы с выбором, неспособность открыться, выбор, который делается из страха остаться одному. Навязчивость и болтливость пересекающиеся с подавлением истинных эмоций. Склонность к созависимым отношениям и частая роль любовницы/любовника.',\
            'Архетип Императрица⚜️\n\n🌝Свет: Вы женственные и красивые, а если Вы мужчина, то очень хорошо понимаете женщин и являетесь их любимчиком. Чувственные, харизматичные, Вам присуща сексуальность, тяга к наслаждению и жизни в роскоши и комфорте. Для Вас очень важна семья и уют, а также деньги. Вы человек-источник, питающий своё окружение!\n«Не знаю, зачем там Вас ваши родители рожали, но меня родили, чтоб я балдела, про все остальное даже слышать не хочу» - девиз всех Императриц.\n\n🌚Тень: властность, жадность, требовательность из серии "мне все должны", проблемы с самооценкой и сексуальностью, зависть и раздражение на все женственное, частая роль любовницы/любовника, склонность к созависимым отношениям и жизни в постоянном напряжении. А также стремление угодить другому и низкая самооценка.',
            'Архетип Император🔱\n\n🌝Свет: Вы ответственны, надёжны, самостоятельны, трудолюбивы, храбры, логичны, мудры и хозяйственны. Вы профессионал в своем деле и прирожденный руководитель и бизнесмен, который вызывает уважение, умеет делегировать и трезво смотрит на вещи.\n\n🌚Тень: жизнь по мужской модели у женщин, дисбаланс семьи и работы у мужчин. Трудоголизм, напряжение и перенапряжение, дисбаланс отношений между мужчиной и женщиной (перепутаны роли). Властность, тирания и излишняя требовательность.'

        ]
# Роли пользователей

- **Создатель проекта** - Может создавать проект, может добавлять людей в проект, может создавать задачи, может редактировать задачи, может изменять статус задачи (все права внутри проекта)

- **Член проекта редактор (исполнитель)** - Может просматривать список задач в проект, может просматривать карточку задачи, может редактировать задачи, может изменять статус задачи, может оставлять комментарии в задаче.

- **Член проекта просмотр** - Может просматривать список задач в проект, может просматривать карточку задачи, не может ничего редактировать

Любой из пользователей может создавать свой проект.

Любой из пользователей может получить роль “Создатель проекта“, в рамках своего созданного проекта.

# USER STORY

- Я, как пользователь (Любой), хочу авторизоваться, чтобы получить доступ к функционалу

- Я, как пользователь (Любой), хочу просматривать список задач на сегодня, чтобы знать, что я должен выполнить сегодня

- Я, как пользователь (Любой), хочу получать уведомления по напоминаниям из задач, чтобы не забывать о них

- Я, как пользователь (Любой), хочу просматривать настраивать свой профиль, чтобы менять Имя, Фамилию, пароль

- Я, как пользователь (Любой,) хочу просматривать список достижений, чтобы иметь мотивацию для выполнения задач

- Я, как пользователь (Любой), хочу просматривать свое расписание в ВУЗе, чтобы оценивать свое время

- Я, как пользователь (Любой), хочу изменять тему интерфейса (светлая/темная), чтобы работать в удобных условиях.

- Я, как пользователь (Любой), хочу видеть диаграмму прогресса выполнения задач в проекте, чтобы оценивать эффективность работы.

- Я, как пользователь (Любой), хочу включать/отключать уведомления для задач и комментариев, чтобы регулировать количество получаемой информации.

- Я, как пользователь (Создатель проекта), хочу создать проект, чтобы добавлять в него других пользователей

- Я, как пользователь (Создатель проекта), хочу создать проект, чтобы заводить в нем задачи для других пользователь

- Я, как пользователь (Создатель проекта), хочу создать задачу, чтобы назначить на нее исполнителя

- Я, как пользователь (Создатель проекта), хочу создавать задачу, чтобы устанавливать дату ее окончания

- Я, как пользователь (Создатель проекта), хочу создавать задачу, чтобы устанавливать дату ее напоминания

- Я, как пользователь (Создатель проекта), хочу создавать задачу, чтобы устанавливать ее приоритет

- Я, как пользователь (Создатель проекта), хочу устанавливать роли (Редактор или Просмотр) для участников, чтобы разделить зоны ответственности.

- Я, как пользователь (Создатель проекта), хочу удалять участников из проекта, чтобы управлять составом команды.

- Я, как пользователь (Создатель проекта, Редактор), хочу просматривать карточку задачи, чтобы менять ее описание

- Я, как пользователь (Создатель проекта, Редактор), хочу просматривать карточку задачи, чтобы менять ее статус

- Я, как пользователь (Создатель проекта, Редактор), хочу просматривать карточку задачи, чтобы добавлять в нее комментарий

- Я, как пользователь (Создатель проекта, Редактор), хочу просматривать карточку задачи, чтобы менять ее приоритет

- Я, как пользователь (Создатель проекта, Редактор, Просмотр), хочу фильтровать задачи по приоритету, чтобы сосредоточиться на более важных задачах.

- Я, как пользователь (Создатель проекта, Редактор, Просмотр), хочу просматривать карточку задачи, чтобы просматривать ее описание

- Я, как пользователь (Создатель проекта, Редактор, Просмотр), хочу просматривать карточку задачи, чтобы просматривать статус задачи

- Я, как пользователь (Создатель проекта, Редактор, Просмотр), хочу просматривать карточку задачи, чтобы просматривать комментарии к задаче

- Я, как пользователь (Создатель проекта, Редактор, Просмотр), хочу просматривать список задач, чтобы видеть даты окончания задач

- Я, как пользователь (Создатель проекта, Редактор, Просмотр), хочу просматривать список задач, чтобы видеть даты окончания задач

# USE CASE
![image](https://github.com/user-attachments/assets/cdde8edb-635b-4979-8472-1df3ba7e5f5f)
![image](https://github.com/user-attachments/assets/206c8a54-1008-4752-96f7-244217c319a9)
![image](https://github.com/user-attachments/assets/448de837-536a-4e52-9fae-58519608f711)




```Plain Text
@startuml
' Диаграмма 1: Базовые функции пользователя
actor "Пользователь" as User

package "Базовые функции пользователя" {
    usecase "Авторизация" as Auth
    usecase "Просмотр списка задач на сегодня" as DailyTasks
    usecase "Получение уведомлений\nпо напоминаниям" as Notifications
    usecase "Настройка профиля" as Profile
    usecase "Просмотр достижений" as Achievements
    usecase "Просмотр расписания ВУЗа" as Schedule
    usecase "Изменение темы интерфейса\n(светлая/темная)" as Theme
    usecase "Просмотр диаграммы прогресса\nвыполнения задач" as ProgressDiagram
    usecase "Включение/отключение уведомлений\nдля задач и комментариев" as ToggleNotifications
}

User --> Auth
User --> DailyTasks
User --> Notifications
User --> Profile
User --> Achievements
User --> Schedule
User --> Theme
User --> ProgressDiagram
User --> ToggleNotifications
@enduml

@startuml
' Диаграмма 2: Функциональность Создателя проекта
actor "Создатель проекта" as Creator

package "Функциональность Создателя проекта" {
    usecase "Создание проекта" as CreateProject
    usecase "Добавление пользователей в проект" as AddUsers
    usecase "Создание задачи" as CreateTask
    usecase "Установка даты окончания задачи" as SetTaskDeadline
    usecase "Установка напоминания для задачи" as SetTaskReminder
    usecase "Установка приоритета задачи" as SetTaskPriority
    usecase "Установка ролей для участников" as SetRoles
    usecase "Удаление участников из проекта" as RemoveUsers
}

Creator --> CreateProject
Creator --> AddUsers
Creator --> CreateTask
CreateTask --> SetTaskDeadline
CreateTask --> SetTaskReminder
CreateTask --> SetTaskPriority
Creator --> SetRoles
Creator --> RemoveUsers
@enduml

@startuml
' Диаграмма 3: Функциональность работы с задачами
actor "Редактор" as Editor
actor "Просмотр" as Viewer
actor "Создатель проекта" as Creator

package "Работа с задачами" {
    usecase "Просмотр карточки задачи" as ViewTask
    usecase "Изменение описания задачи" as EditTaskDescription
    usecase "Изменение статуса задачи" as EditTaskStatus
    usecase "Добавление комментариев в задачу" as AddComments
    usecase "Изменение приоритета задачи" as EditTaskPriority
    usecase "Фильтрация задач по приоритету" as FilterTasks
    usecase "Просмотр списка задач с датами\nокончания" as ViewTaskList
    usecase "Просмотр описания задачи" as ViewDescription
    usecase "Просмотр статуса задачи" as ViewStatus
    usecase "Просмотр комментариев к задаче" as ViewComments
}

Creator --> ViewTask
Creator --> EditTaskDescription
Creator --> EditTaskStatus
Creator --> AddComments
Creator --> EditTaskPriority
Creator --> FilterTasks
Creator --> ViewTaskList

Editor --> ViewTask
Editor --> EditTaskDescription
Editor --> EditTaskStatus
Editor --> AddComments
Editor --> EditTaskPriority
Editor --> FilterTasks
Editor --> ViewTaskList

Viewer --> ViewTask
Viewer --> FilterTasks
Viewer --> ViewTaskList

ViewTask --> ViewDescription
ViewTask --> ViewStatus
ViewTask --> ViewComments
@enduml
```

# План реализации

1. **Реализация боковой панели**

Блоки боковой панели
| **Номер элемента** | **Название элемента** | **Описание элемента**                                                                                                                                                                                                                                               |
|---------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                   | Профиль              | Выводим иконку + имя пользователя. При нажатии на профиль открывается выпадающий список, состоящий из: 1. Настройки 2. Статистика 3. Выполненные задачи 4. Выйти                                                                                                  |
| 2                   | Уведомление          | Значок уведомления рядом с профилем. В данный колокольчик приходят уведомления по созданным заданиям и напоминаниям. При приходе уведомления появляется цифра на значке.                                                                                         |
| 3                   | Добавить задачу      | При нажатии на кнопку открывается Поп-ап с созданием задачи. Данный элемент должен быть зеленого цвета и быть больше других элементов.                                                                                                                            |
| 4                   | Сегодня              | Выводим все задачи, созданные на сегодня. Данная страница открывается пользователю первой.                                                                                                                                                                       |
| 5                   | Расписание вуза      | Выводим расписание ВУЗа ИКТИБ ЮФУ. API [о сайте](https://ictis-alex.b).                                                                                                                                                                                           |
| 6                   | Достижения           | Выводим список достижений. Сначала в списке выводим полученные достижения.                                                                                                                                                                                        |
| 7                   | Проекты              | Данная надпись является заголовком. Рядом с надписью есть знак "+", который используется для создания нового проекта. Также можно скрывать/разворачивать данный блок, при нажатии на ">".                                                                         |
| 7.1                 | Название проекта     | При нажатии на название проекта открывается его наполнение, где пользователь может увидеть все задачи на все дни, созданные в рамках данного проекта. Рядом с названием проекта есть иконка "...". При нажатии на иконку открывается меню: 1. Редактировать - форма создания задачи 2. Выполненные задачи 3. Удалить - удалить проект |


1. **Нажатие на кнопку создать задачу - Создавать задачу может только Создатель проекта и Редактор.**

При нажатии на кнопку создать задачу открывается Поп-ап в котором можно создать задачу.

Описание элементов формы

||||
|-|-|-|
|**Номер элемента**|**Название элемента**|**Описание элемента**|
|1|Название задачи|Строка ввода. Обязательное поле. В данном поле пользователь вводит название задачи.|
|2|Описание задачи|Поле ввода (делаем его широким). Необязательное поле. В данном поле пользователь вводит описание задачи|
|3|Срок (Дата)|Календарь. Обязательное поле. Пользователь выбирает дату, до которой пользователь должен выполнить задачу. Задача в списке будет находится в дате, которая выбрана в данном поле.|
|4|Приоритет|Выпадающий список с моновыбором. Необязательное поле. Изначально задаем приоритет 1. Для выбора есть приоритеты 1-4. Чем выше приоритет, тем выше задача в списке на данный день.|
|5|Напоминания|Календарь. Необязательное поле. Пользователь выбирает дату, когда придет уведомление, напоминающее, что нужно сделать задачу|
|6|Проект|Выпадающий список с моновыбором и возможностью поиска. Обязательное поле. Пользователь выбирает в каком проекте создать задачу.|
|7|Исполнитель|Выпадающий список с моновыбором и возможностью поиска. Возможность выбрать исполнителя, среди пользователей, которые есть в проекте.|
|8|Отменить|Кнопка для отмены|
|9|Добавить задачу|Кнопка для создания задачи. Имеет зеленый цвет.|

1. **Создание проекта**

При нажатии на + рядом с Проект (п.1.7) открывается Поп-ап с созданием проекта.

Описание элементов формы

||||
|-|-|-|
|**Номер элемента**|**Название элемента**|**Описание элемента**|
|1|Добавить проект|Название блока|
|2|Крестик|Закрытие формы|
|3|Имя|Поле ввода. Обязательное поле. В данном поле пользователь вводит название проекта|
|4|Пользователи|Возможность добавления пользователя в проект по почте при создании проекта.|
|5|Отмена|Кнопка для отмены|
|6|Добавить|Кнопка для создания проекта. Имеет зеленый цвет.|

1. **Список задач | Проект**

Заголовок - Название проекта

Ниже выводим количество задач, которое есть в списке

Выводим список задач по датам. С возможностью создать задачу в данную дату

**При нажатии на чекбокс (можно выбирать несколько чекбоксов разом) появляется кнопка “Закрыть задачи“ рядом с Заголовком (Название проекта). При нажатии на кнопку открывается поп-ап. Заголовок - Закрыть задачу. Две кнопки - Да / Нет.**

Пример:

![image](https://github.com/user-attachments/assets/c1e69733-9d93-4778-9267-2be85d7f21f8)


Задачи в списке выводятся согласно их приоритетам. Задачи с высшим приоритетом выводятся выше. Если у задач одинаковый приоритет, то выводим согласно алфавиту от А-Я.

В списке задач, на каждой строчке задачи выводится исполнитель.

Рядом с название задачи выводим Выпадающий список с моновыбором статусов задачи. Возможность изменять статус есть у Создателя проекта и Редактора.

1. **Список задач | Сегодня**

Заголовок - Сегодня

Ниже выводим количество задач, которое есть в списке

Выводим список задач по датам.

**При нажатии на чекбокс (можно выбирать несколько чекбоксов разом) появляется кнопка “Закрыть задачи“ рядом с Заголовком (Название проекта). При нажатии на кнопку открывается поп-ап. Заголовок - Закрыть задачу. Две кнопки - Да / Нет.**

![image](https://github.com/user-attachments/assets/769b7380-f164-4d99-be51-798663bab83e)


Задачи в списке выводятся согласно их приоритетам. Задачи с высшим приоритетом выводятся выше. Если у задач одинаковый приоритет, то выводим согласно алфавиту от А-Я.

В списке задач, на каждой строчке задачи выводится исполнитель.

Рядом с название задачи выводим Выпадающий список с моновыбором статусов задачи. Возможность изменять статус есть у Создателя проекта и Редактора.

**В самом верху выводим просроченные задачи (нынешняя дата > дата окончания задачи)**

Заголовок - Просроченные задачи. Под названием задачи пишется насколько просрачена задача

Пример:

1. **Карточка задачи**
При нажатии на название задачи открывается карточка задачи. Данная карточка состоит из 2 блоков - Блок с Названием/Статусом/Описанием/Возможность добавлять подзадачи/Комментарием и Блок с Проектом/Исполнителем/

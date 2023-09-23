from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

# Create your views here.
def index(request):
    return HttpResponsePermanentRedirect('home/')

def home(request):
    return render(request, 'index.html')

def persona(req,id):
    id=int(id)
    name=['Балиан','Сибилла','Саладин','Ги де Лузиньян']
    description = ['Балиан II Ибелин — крестоносец из рода Ибелинов.Командовал обороной Иерусалима во время штурма '
                   'города войсками Саладина 20 сентября — 2 октября 1187 года. Сдал город на почётных условиях, '
                   'после того, как пригрозил Саладину разрушить мусульманские святыни.', 'Сибилла Иерусалимская (Сибилла Анжуйская,'
                ' около 1160—1190) — королева Иерусалима с 1186 года', 'Салах ад-Дин— султан Египта и Сирии и др., военачальник, '
                ' мусульманский лидер XII века. Курд по происхождению. Основатель династии Айюбидов, которая в период своего расцвета'
                ' правила Египтом, Сирией, Ираком, Хиджазом и Йеменом.','Ги (Гвидо) де Лузиньян — видная личность в истории крестовых'
                ' походов и государств крестоносцев, французский рыцарь из династии Лузиньянов, король Иерусалима в 1186—1192 годах '
                '(как соправитель жены Сибиллы), сеньор Кипра с 1192 года. Сын Гуго VIII де Лузиньяна и Бургонь де Ранкон.']
    akter=['Орландо Блум','Ева Грин','Гассан Массуд','Мартон Чокаш',]
    imgs=['https://e7.pngegg.com/pngimages/735/27/png-clipart-orlando-bloom-at-the-movies-orlando-bloom.png', 'https://i.pinimg.com/originals/5e/4f/a9/5e4fa9b4b9f21e82630f1850d9343b72.png', 'https://i.pinimg.com/originals/7c/1e/dc/7c1edc0480535596b4b225581c2f4516.png', 'https://i.pinimg.com/originals/b7/07/c7/b707c7fb184320371fb17c4b92715dd5.png']
    ssilka=['https://ru.wikipedia.org/wiki/Блум,_Орландо' ,'https://ru.wikipedia.org/wiki/Грин,_Ева','https://ru.wikipedia.org/wiki/Масуд,_Гассан','https://ru.wikipedia.org/wiki/Чокаш,_Мартон',]
    data={'n1':name[id],'n2':description[id],'n3':akter[id],'n4':imgs[id],'n5':ssilka[id]}
    return render(req,'persona.html',context=data)

import logging
from django.contrib.auth.models import User
from ppd.models import Like, MyChoiceIni, Viewing, ThesisViewing, ThesisLike

from django.template.defaulttags import register

logger = logging.getLogger(__name__)


# @register.filter(name='lookup')
# def lookup(value, arg):
#  return value.get(arg) 
@register.filter
def get_item(dictionary, key):
    # logger.error(f'vuiiii {dictionary}')
    return dictionary[0].get(key)


@register.filter
def get_like(self, u):
    # print('looo')
    # logger.error(f'nop {self.__name__}')
    #print(self.__class__.__name__)
    nm = self.__class__.__name__
    if nm == 'Message':
        return Like.objects.filter(father=self, author=u)
    elif nm == 'Initiative':
        pass
    elif nm == 'Thesis':
        #print(ThesisLike.objects.filter(father=self, author=u))
        return ThesisLike.objects.filter(father=self, author=u)

        # return Like.objects.filter(f=self, author=u)


@register.filter
def get_like_uni(self, u):
    # logger.error(f'nop {self}')
    return Like.objects.filter(father_pic=self, author=u)


@register.filter
def get_like_userrep(self, u):
    # print(self.id)
    return Like.objects.filter(father_userreply=self, author=u)


@register.filter
def get_viewed(self, u):
    # print(self.id)
    return Viewing.objects.filter(father=self, author=u)


@register.filter
def get_viewed_thesis(self, u):
    # print(self.id)
    return ThesisViewing.objects.filter(father=self, author=u)


# register.filter('get_like', get_like)


@register.filter
def its_my_choice(self, u):
    #print(self.id)
    #print(u)
    try:
        vv = MyChoiceIni.objects.get(father=self, author=u)
        return vv.choice.pk
    except:
        return 0
    # return Like.objects.filter(father_userreply=self,author=u)

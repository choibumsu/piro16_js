import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.templatetags.static import static
from django.views.decorators.http import require_GET, require_POST


def home(request):
    context = {
        'name': 'bbamsu211',
        'profile': static('images/profile.jpeg'),
        'content_images': json.dumps([
            static('images/react.png'),
            static('images/vue.png'),
            static('images/svelte.png')
        ]),
        'content': '프론트엔드 프레임워크 추천해주세요!',
        'like': 100,
        'is_like': False,
        'comments': json.dumps([
            {
                'id': 1,
                'user': 'mmmaxkim',
                'text': '리액트 추천합니다~'
            },
            {
                'id': 2,
                'user': '_sulmo',
                'text': 'Vue가 제일 쉽지 않나요?'
            },
            {
                'id': 3,
                'user': '_neulhan',
                'text': '스벨트 써보실래요?'
            },
        ])
    }
    return render(request, 'app/home.html', context)


@require_GET
def get_comments_api(request):
    comments = [
        {
            'id': 4,
            'user': 'bbamsu211',
            'text': '@mmmaxkim 감사합니다!'
        },
        {
            'id': 5,
            'user': 'bbamsu211',
            'text': '@_sulmo 감사합니다!'
        },
        {
            'id': 6,
            'user': 'bbamsu211',
            'text': '@_neulhan 감사합니다!'
        }
    ]

    context = {
        'comments': comments
    }

    return JsonResponse(context)


def get_param(request, key, default_value=None):
    request_body = json.loads(request.body.decode('utf-8'))
    return request_body[key] if key in request_body else default_value


@require_POST
def post_comment_api(request):
    comment = get_param(request, 'comment', '')
    user = get_param(request, 'user', '')
    print(comment, user)

    context = {
        'id': 7
    }

    return JsonResponse(context)

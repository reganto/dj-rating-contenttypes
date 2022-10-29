from posts.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")
    rates_count = serializers.SerializerMethodField()
    rates_average = serializers.SerializerMethodField()
    current_user_rate = serializers.SerializerMethodField()

    def get_rates_count(self, obj):
        return obj.rates_count

    def get_rates_average(self, obj):
        return round(obj.rates_average, 1)

    def get_current_user_rate(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return obj.current_user_rate(user)

    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "author",
            "rates_count",
            "rates_average",
            "current_user_rate",
        )

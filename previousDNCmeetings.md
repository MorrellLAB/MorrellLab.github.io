---
layout: hidden_page
hidden_title: Previous Does[0]Compute Meetings
permalink: /previousDNC/
---

{% assign site_year = site.time | date: "%Y" %}
{% assign site_day = site.time | date: "%j" %}

<div class="home">
    <ul class="posts">
        {% for post in site.compute reversed%}
            {% assign post_year = post.meet_date | date: "%Y" %}
            {% assign post_day = post.meet_date | date: "%j" %}
            {% if  post_year <= site_year %}
                {% if post_day <= site_day %}
                    <li>
                        <span class="post-date">{{ post.meet_date | date: "%b %-d, %Y" }}</span>
                        <a href="{{ post.url }}">{{ post.topic }}</a><br />
                        <span class="post-content">
                            Lead by:
                            {% if post.leaders %}
                                {{ post.leaders }}
                            {% else %}
                                <em>To be determined</em>
                            {% endif %}
                        </span>
                    </li>
                {% endif %}
            {% endif %}
        {% endfor %}
    </ul>
</div>

<!-- Start Google Analytics -->
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-19694768-1']);
_gaq.push(['_trackPageview']);
(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<!-- End Google Analytics -->
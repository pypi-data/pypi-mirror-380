# do not pre-load
import re

__all__ = ['prog_disclose']


def prog_disclose(template, classname=None):
    if classname is None:
        classname = ' bg-secondary-subtle'
    else:
        classname = ' ' + classname.strip()
    the_id = re.sub(r'[^A-Za-z0-9]', '', template.instanceName)
    return """\
<a class="collapsed" data-bs-toggle="collapse" href="#{the_id}" role="button" aria-expanded="false" aria-controls="collapseExample"><span class="pdcaretopen"><i class="fa-solid fa-caret-down"></i></span><span class="pdcaretclosed"><i class="fa-solid fa-caret-right"></i></span> {the_subject}</a>
<div class="collapse" id="{the_id}"><div class="card card-body{the_classname} pb-1">{the_content}</div></div>\
""".format(the_id=the_id, the_subject=template.subject_as_html(trim=True), the_classname=classname, the_content=template.content_as_html())

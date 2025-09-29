{% import 'src/components/macros.jinja2' as macros %}
//! {{ctx.module_comment}}

{{macros.includes(ctx)}}

{{ctx.comment}}
#[repr(transparent)]
#[derive(Copy, Clone, Eq, PartialEq)]
pub struct {{ctx.type_name}}(u{{ctx.regwidth}});

unsafe impl Send for {{ctx.type_name}} {}
unsafe impl Sync for {{ctx.type_name}} {}

impl core::default::Default for {{ctx.type_name}} {
    fn default() -> Self {
        Self(0x{{"%X" % ctx.reset_val}})
    }
}

impl crate::reg::Register for {{ctx.type_name}} {
    type Regwidth = u{{ctx.regwidth}};
    type Accesswidth = u{{ctx.accesswidth}};

    unsafe fn from_raw(val: Self::Regwidth) -> Self {
        Self(val)
    }

    fn to_raw(self) -> Self::Regwidth {
        self.0
    }
}

impl {{ctx.type_name}} {
{% for field in ctx.fields %}
    pub const {{field.inst_name|upper}}_OFFSET: usize = {{field.bit_offset}};
    pub const {{field.inst_name|upper}}_WIDTH: usize = {{field.width}};
    pub const {{field.inst_name|upper}}_MASK: u{{ctx.regwidth}} = 0x{{"%X" % field.mask}};

    {{field.comment | indent()}}
    #[inline(always)]
    {% set return_type = "Option<" ~ field.encoding ~ ">" if field.encoding else field.primitive %}
    {% if "R" in field.access %}pub {% endif -%}
    const fn {{field.inst_name}}(&self) -> {{return_type}} {
        let val = (self.0 >> Self::{{field.inst_name|upper}}_OFFSET) & Self::{{field.inst_name|upper}}_MASK;
        {% if field.encoding is not none %}
        {{field.encoding}}::from_bits(val as {{field.primitive}})
        {% elif field.primitive == "bool" %}
        val != 0
        {% elif field.primitive != "u" ~ ctx.regwidth %}
        val as {{field.primitive}}
        {% else %}
        val
        {% endif %}
    }

    {% if "W" in field.access %}
    {{field.comment | indent()}}
    #[inline(always)]
    {% set input_type = field.encoding if field.encoding else field.primitive %}
    pub const fn set_{{field.inst_name}}(&mut self, val: {{input_type}}) {
        {% if field.encoding %}
        let val = val.bits() as u{{ctx.regwidth}};
        {% else %}
        let val = val as u{{ctx.regwidth}};
        {% endif %}
        self.0 = (self.0 & !(Self::{{field.inst_name|upper}}_MASK << Self::{{field.inst_name|upper}}_OFFSET)) | ((val & Self::{{field.inst_name|upper}}_MASK) << Self::{{field.inst_name|upper}}_OFFSET);
    }
    {% endif %}

{% endfor %}
}

impl core::fmt::Debug for {{ctx.type_name}} {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        f.debug_struct("{{ctx.type_name}}")
            {% for field in ctx.fields %}
            .field("{{field.inst_name}}", &self.{{field.inst_name}}())
            {% endfor %}
            .finish()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_default() {
        let reg = {{ctx.type_name}}::default();
        {% for field in ctx.fields %}
        assert_eq!(reg.{{field.inst_name}}(), {{field.reset_val}});
        {% endfor %}
    }
}

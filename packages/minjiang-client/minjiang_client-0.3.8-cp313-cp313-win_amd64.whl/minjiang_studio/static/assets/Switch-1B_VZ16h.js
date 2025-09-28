import{am as A,aq as t,ap as K,ao as o,an as I,cB as O,d as se,bh as P,Q as n,b_ as f,cz as ce,bS as de,ar as ue,ax as E,dT as he,cb as be,r as j,aH as fe,aG as ve,J as z,az as v,by as H,bX as r,aA as ge,aM as M}from"./index-CvCv8tjC.js";const we=A("switch",`
 height: var(--n-height);
 min-width: var(--n-width);
 vertical-align: middle;
 user-select: none;
 -webkit-user-select: none;
 display: inline-flex;
 outline: none;
 justify-content: center;
 align-items: center;
`,[t("children-placeholder",`
 height: var(--n-rail-height);
 display: flex;
 flex-direction: column;
 overflow: hidden;
 pointer-events: none;
 visibility: hidden;
 `),t("rail-placeholder",`
 display: flex;
 flex-wrap: none;
 `),t("button-placeholder",`
 width: calc(1.75 * var(--n-rail-height));
 height: var(--n-rail-height);
 `),A("base-loading",`
 position: absolute;
 top: 50%;
 left: 50%;
 transform: translateX(-50%) translateY(-50%);
 font-size: calc(var(--n-button-width) - 4px);
 color: var(--n-loading-color);
 transition: color .3s var(--n-bezier);
 `,[O({left:"50%",top:"50%",originalTransform:"translateX(-50%) translateY(-50%)"})]),t("checked, unchecked",`
 transition: color .3s var(--n-bezier);
 color: var(--n-text-color);
 box-sizing: border-box;
 position: absolute;
 white-space: nowrap;
 top: 0;
 bottom: 0;
 display: flex;
 align-items: center;
 line-height: 1;
 `),t("checked",`
 right: 0;
 padding-right: calc(1.25 * var(--n-rail-height) - var(--n-offset));
 `),t("unchecked",`
 left: 0;
 justify-content: flex-end;
 padding-left: calc(1.25 * var(--n-rail-height) - var(--n-offset));
 `),K("&:focus",[t("rail",`
 box-shadow: var(--n-box-shadow-focus);
 `)]),o("round",[t("rail","border-radius: calc(var(--n-rail-height) / 2);",[t("button","border-radius: calc(var(--n-button-height) / 2);")])]),I("disabled",[I("icon",[o("rubber-band",[o("pressed",[t("rail",[t("button","max-width: var(--n-button-width-pressed);")])]),t("rail",[K("&:active",[t("button","max-width: var(--n-button-width-pressed);")])]),o("active",[o("pressed",[t("rail",[t("button","left: calc(100% - var(--n-offset) - var(--n-button-width-pressed));")])]),t("rail",[K("&:active",[t("button","left: calc(100% - var(--n-offset) - var(--n-button-width-pressed));")])])])])])]),o("active",[t("rail",[t("button","left: calc(100% - var(--n-button-width) - var(--n-offset))")])]),t("rail",`
 overflow: hidden;
 height: var(--n-rail-height);
 min-width: var(--n-rail-width);
 border-radius: var(--n-rail-border-radius);
 cursor: pointer;
 position: relative;
 transition:
 opacity .3s var(--n-bezier),
 background .3s var(--n-bezier),
 box-shadow .3s var(--n-bezier);
 background-color: var(--n-rail-color);
 `,[t("button-icon",`
 color: var(--n-icon-color);
 transition: color .3s var(--n-bezier);
 font-size: calc(var(--n-button-height) - 4px);
 position: absolute;
 left: 0;
 right: 0;
 top: 0;
 bottom: 0;
 display: flex;
 justify-content: center;
 align-items: center;
 line-height: 1;
 `,[O()]),t("button",`
 align-items: center; 
 top: var(--n-offset);
 left: var(--n-offset);
 height: var(--n-button-height);
 width: var(--n-button-width-pressed);
 max-width: var(--n-button-width);
 border-radius: var(--n-button-border-radius);
 background-color: var(--n-button-color);
 box-shadow: var(--n-button-box-shadow);
 box-sizing: border-box;
 cursor: inherit;
 content: "";
 position: absolute;
 transition:
 background-color .3s var(--n-bezier),
 left .3s var(--n-bezier),
 opacity .3s var(--n-bezier),
 max-width .3s var(--n-bezier),
 box-shadow .3s var(--n-bezier);
 `)]),o("active",[t("rail","background-color: var(--n-rail-color-active);")]),o("loading",[t("rail",`
 cursor: wait;
 `)]),o("disabled",[t("rail",`
 cursor: not-allowed;
 opacity: .5;
 `)])]),me=Object.assign(Object.assign({},E.props),{size:{type:String,default:"medium"},value:{type:[String,Number,Boolean],default:void 0},loading:Boolean,defaultValue:{type:[String,Number,Boolean],default:!1},disabled:{type:Boolean,default:void 0},round:{type:Boolean,default:!0},"onUpdate:value":[Function,Array],onUpdateValue:[Function,Array],checkedValue:{type:[String,Number,Boolean],default:!0},uncheckedValue:{type:[String,Number,Boolean],default:!1},railStyle:Function,rubberBand:{type:Boolean,default:!0},onChange:[Function,Array]});let k;const ye=se({name:"Switch",props:me,slots:Object,setup(e){k===void 0&&(typeof CSS<"u"?typeof CSS.supports<"u"?k=CSS.supports("width","max(1px)"):k=!1:k=!0);const{mergedClsPrefixRef:S,inlineThemeDisabled:m}=ue(e),V=E("Switch","-switch",we,he,e,S),l=be(e),{mergedSizeRef:$,mergedDisabledRef:h}=l,p=j(e.defaultValue),B=fe(e,"value"),b=ve(B,p),y=z(()=>b.value===e.checkedValue),g=j(!1),i=j(!1),s=z(()=>{const{railStyle:a}=e;if(a)return a({focused:i.value,checked:y.value})});function c(a){const{"onUpdate:value":C,onChange:_,onUpdateValue:R}=e,{nTriggerFormInput:F,nTriggerFormChange:T}=l;C&&M(C,a),R&&M(R,a),_&&M(_,a),p.value=a,F(),T()}function X(){const{nTriggerFormFocus:a}=l;a()}function L(){const{nTriggerFormBlur:a}=l;a()}function Y(){e.loading||h.value||(b.value!==e.checkedValue?c(e.checkedValue):c(e.uncheckedValue))}function q(){i.value=!0,X()}function G(){i.value=!1,L(),g.value=!1}function J(a){e.loading||h.value||a.key===" "&&(b.value!==e.checkedValue?c(e.checkedValue):c(e.uncheckedValue),g.value=!1)}function Q(a){e.loading||h.value||a.key===" "&&(a.preventDefault(),g.value=!0)}const U=z(()=>{const{value:a}=$,{self:{opacityDisabled:C,railColor:_,railColorActive:R,buttonBoxShadow:F,buttonColor:T,boxShadowFocus:Z,loadingColor:ee,textColor:te,iconColor:ae,[v("buttonHeight",a)]:d,[v("buttonWidth",a)]:ie,[v("buttonWidthPressed",a)]:ne,[v("railHeight",a)]:u,[v("railWidth",a)]:x,[v("railBorderRadius",a)]:oe,[v("buttonBorderRadius",a)]:re},common:{cubicBezierEaseInOut:le}}=V.value;let N,W,D;return k?(N=`calc((${u} - ${d}) / 2)`,W=`max(${u}, ${d})`,D=`max(${x}, calc(${x} + ${d} - ${u}))`):(N=H((r(u)-r(d))/2),W=H(Math.max(r(u),r(d))),D=r(u)>r(d)?x:H(r(x)+r(d)-r(u))),{"--n-bezier":le,"--n-button-border-radius":re,"--n-button-box-shadow":F,"--n-button-color":T,"--n-button-width":ie,"--n-button-width-pressed":ne,"--n-button-height":d,"--n-height":W,"--n-offset":N,"--n-opacity-disabled":C,"--n-rail-border-radius":oe,"--n-rail-color":_,"--n-rail-color-active":R,"--n-rail-height":u,"--n-rail-width":x,"--n-width":D,"--n-box-shadow-focus":Z,"--n-loading-color":ee,"--n-text-color":te,"--n-icon-color":ae}}),w=m?ge("switch",z(()=>$.value[0]),U,e):void 0;return{handleClick:Y,handleBlur:G,handleFocus:q,handleKeyup:J,handleKeydown:Q,mergedRailStyle:s,pressed:g,mergedClsPrefix:S,mergedValue:b,checked:y,mergedDisabled:h,cssVars:m?void 0:U,themeClass:w==null?void 0:w.themeClass,onRender:w==null?void 0:w.onRender}},render(){const{mergedClsPrefix:e,mergedDisabled:S,checked:m,mergedRailStyle:V,onRender:l,$slots:$}=this;l==null||l();const{checked:h,unchecked:p,icon:B,"checked-icon":b,"unchecked-icon":y}=$,g=!(P(B)&&P(b)&&P(y));return n("div",{role:"switch","aria-checked":m,class:[`${e}-switch`,this.themeClass,g&&`${e}-switch--icon`,m&&`${e}-switch--active`,S&&`${e}-switch--disabled`,this.round&&`${e}-switch--round`,this.loading&&`${e}-switch--loading`,this.pressed&&`${e}-switch--pressed`,this.rubberBand&&`${e}-switch--rubber-band`],tabindex:this.mergedDisabled?void 0:0,style:this.cssVars,onClick:this.handleClick,onFocus:this.handleFocus,onBlur:this.handleBlur,onKeyup:this.handleKeyup,onKeydown:this.handleKeydown},n("div",{class:`${e}-switch__rail`,"aria-hidden":"true",style:V},f(h,i=>f(p,s=>i||s?n("div",{"aria-hidden":!0,class:`${e}-switch__children-placeholder`},n("div",{class:`${e}-switch__rail-placeholder`},n("div",{class:`${e}-switch__button-placeholder`}),i),n("div",{class:`${e}-switch__rail-placeholder`},n("div",{class:`${e}-switch__button-placeholder`}),s)):null)),n("div",{class:`${e}-switch__button`},f(B,i=>f(b,s=>f(y,c=>n(ce,null,{default:()=>this.loading?n(de,{key:"loading",clsPrefix:e,strokeWidth:20}):this.checked&&(s||i)?n("div",{class:`${e}-switch__button-icon`,key:s?"checked-icon":"icon"},s||i):!this.checked&&(c||i)?n("div",{class:`${e}-switch__button-icon`,key:c?"unchecked-icon":"icon"},c||i):null})))),f(h,i=>i&&n("div",{key:"checked",class:`${e}-switch__checked`},i)),f(p,i=>i&&n("div",{key:"unchecked",class:`${e}-switch__unchecked`},i)))))}});export{ye as N};

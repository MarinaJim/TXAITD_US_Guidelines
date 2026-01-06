import random


index_html = r"""
<html>

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type">
    <style type="text/css">
        .lst-kix_j4kjsgd1usr2-4>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-4
        }

        .lst-kix_czgqhruwmsu1-7>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-7
        }

        ul.lst-kix_vnz7yp9fgs5j-7 {
            list-style-type: none
        }

        ul.lst-kix_vnz7yp9fgs5j-8 {
            list-style-type: none
        }

        .lst-kix_p4sqbq9t8yiu-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_p4sqbq9t8yiu-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_pebn44bjo6s-0>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-0
        }

        ol.lst-kix_pebn44bjo6s-3.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-3 0
        }

        ol.lst-kix_dnjp9siocxu4-4.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-4 0
        }

        ul.lst-kix_caqan9w5v6s3-1 {
            list-style-type: none
        }

        ul.lst-kix_caqan9w5v6s3-0 {
            list-style-type: none
        }

        ul.lst-kix_caqan9w5v6s3-8 {
            list-style-type: none
        }

        ul.lst-kix_caqan9w5v6s3-7 {
            list-style-type: none
        }

        .lst-kix_dnjp9siocxu4-1>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-1
        }

        ul.lst-kix_caqan9w5v6s3-6 {
            list-style-type: none
        }

        ol.lst-kix_96dsu66so6uk-3.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-3 0
        }

        ul.lst-kix_caqan9w5v6s3-5 {
            list-style-type: none
        }

        ul.lst-kix_caqan9w5v6s3-4 {
            list-style-type: none
        }

        ul.lst-kix_caqan9w5v6s3-3 {
            list-style-type: none
        }

        ul.lst-kix_caqan9w5v6s3-2 {
            list-style-type: none
        }

        .lst-kix_84c8l1w2s6ae-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_8szmi080x45v-5 {
            list-style-type: none
        }

        ul.lst-kix_8szmi080x45v-6 {
            list-style-type: none
        }

        .lst-kix_84c8l1w2s6ae-6>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_8szmi080x45v-3 {
            list-style-type: none
        }

        ul.lst-kix_8szmi080x45v-4 {
            list-style-type: none
        }

        .lst-kix_84c8l1w2s6ae-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_8szmi080x45v-1 {
            list-style-type: none
        }

        ul.lst-kix_8szmi080x45v-2 {
            list-style-type: none
        }

        ul.lst-kix_8szmi080x45v-0 {
            list-style-type: none
        }

        ol.lst-kix_pebn44bjo6s-8.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-8 0
        }

        ol.lst-kix_jb60d078zlbw-4.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-4 0
        }

        ul.lst-kix_8szmi080x45v-7 {
            list-style-type: none
        }

        .lst-kix_czgqhruwmsu1-3>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-3
        }

        ul.lst-kix_8szmi080x45v-8 {
            list-style-type: none
        }

        .lst-kix_jb60d078zlbw-3>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-3
        }

        .lst-kix_84c8l1w2s6ae-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_8szmi080x45v-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_8szmi080x45v-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_jb60d078zlbw-6>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-6
        }

        .lst-kix_pebn44bjo6s-4>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-4
        }

        .lst-kix_pebn44bjo6s-7>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-7
        }

        .lst-kix_8szmi080x45v-8>li:before {
            content: "\0025a0   "
        }

        ol.lst-kix_96dsu66so6uk-8.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-8 0
        }

        .lst-kix_96dsu66so6uk-3>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-3
        }

        .lst-kix_96dsu66so6uk-6>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-6
        }

        .lst-kix_cdehrceqlghv-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_8szmi080x45v-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_lititpuapscg-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_lititpuapscg-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_8szmi080x45v-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_5810dfl06zcs-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_5810dfl06zcs-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_8szmi080x45v-1>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_czgqhruwmsu1-2.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-2 0
        }

        .lst-kix_cdehrceqlghv-7>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_pebn44bjo6s-5.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-5 0
        }

        .lst-kix_5810dfl06zcs-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_84c8l1w2s6ae-3>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_jb60d078zlbw-0 {
            list-style-type: none
        }

        .lst-kix_lititpuapscg-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_lititpuapscg-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_84c8l1w2s6ae-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_5810dfl06zcs-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_f5jwmjmtc1n3-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_caqan9w5v6s3-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_caqan9w5v6s3-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_pebn44bjo6s-8>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-8
        }

        .lst-kix_f5jwmjmtc1n3-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_f5jwmjmtc1n3-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_uptd83zf0nec-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_uptd83zf0nec-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_f5jwmjmtc1n3-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_uptd83zf0nec-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_pebn44bjo6s-3>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-3
        }

        .lst-kix_jb60d078zlbw-7>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-7
        }

        .lst-kix_caqan9w5v6s3-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_caqan9w5v6s3-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_2rafwmrkqedl-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_msgq2u1dh4zt-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_caqan9w5v6s3-4>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_jb60d078zlbw-1.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-1 0
        }

        .lst-kix_uptd83zf0nec-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_msgq2u1dh4zt-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_2rafwmrkqedl-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_f5jwmjmtc1n3-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_p4sqbq9t8yiu-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_p4sqbq9t8yiu-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_j4kjsgd1usr2-2>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-2, lower-roman) ". "
        }

        .lst-kix_2rafwmrkqedl-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_p4sqbq9t8yiu-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_p4sqbq9t8yiu-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_msgq2u1dh4zt-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_dnjp9siocxu4-8>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-8
        }

        .lst-kix_j4kjsgd1usr2-0>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-0, decimal) ". "
        }

        .lst-kix_2rafwmrkqedl-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_9x4ghkqosc4u-7>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_vnz7yp9fgs5j-1 {
            list-style-type: none
        }

        .lst-kix_msgq2u1dh4zt-6>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_vnz7yp9fgs5j-2 {
            list-style-type: none
        }

        ul.lst-kix_vnz7yp9fgs5j-0 {
            list-style-type: none
        }

        ul.lst-kix_vnz7yp9fgs5j-5 {
            list-style-type: none
        }

        ul.lst-kix_vnz7yp9fgs5j-6 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-0.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-0 0
        }

        ul.lst-kix_vnz7yp9fgs5j-3 {
            list-style-type: none
        }

        .lst-kix_9x4ghkqosc4u-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_9x4ghkqosc4u-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_vnz7yp9fgs5j-4 {
            list-style-type: none
        }

        .lst-kix_msgq2u1dh4zt-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_9x4ghkqosc4u-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_96dsu66so6uk-0>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-0
        }

        ol.lst-kix_96dsu66so6uk-6.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-6 0
        }

        .lst-kix_dnjp9siocxu4-8>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-8, lower-roman) ". "
        }

        .lst-kix_czgqhruwmsu1-2>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-2, lower-roman) ". "
        }

        .lst-kix_h257s328suf3-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_h257s328suf3-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_czgqhruwmsu1-3>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-3, decimal) ". "
        }

        .lst-kix_dnjp9siocxu4-7>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-7, lower-latin) ". "
        }

        ul.lst-kix_lysqczbphrer-8 {
            list-style-type: none
        }

        .lst-kix_h257s328suf3-3>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_lysqczbphrer-6 {
            list-style-type: none
        }

        ul.lst-kix_lititpuapscg-8 {
            list-style-type: none
        }

        ul.lst-kix_lysqczbphrer-7 {
            list-style-type: none
        }

        .lst-kix_czgqhruwmsu1-6>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-6, decimal) ". "
        }

        ul.lst-kix_lysqczbphrer-4 {
            list-style-type: none
        }

        .lst-kix_dnjp9siocxu4-4>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-4, lower-latin) ". "
        }

        ul.lst-kix_lysqczbphrer-5 {
            list-style-type: none
        }

        ul.lst-kix_lysqczbphrer-2 {
            list-style-type: none
        }

        ul.lst-kix_lysqczbphrer-3 {
            list-style-type: none
        }

        .lst-kix_j4kjsgd1usr2-5>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-5, lower-roman) ". "
        }

        ul.lst-kix_lysqczbphrer-0 {
            list-style-type: none
        }

        ul.lst-kix_lititpuapscg-2 {
            list-style-type: none
        }

        ul.lst-kix_lysqczbphrer-1 {
            list-style-type: none
        }

        ul.lst-kix_lititpuapscg-3 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-1.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-1 0
        }

        ul.lst-kix_lititpuapscg-0 {
            list-style-type: none
        }

        ul.lst-kix_lititpuapscg-1 {
            list-style-type: none
        }

        .lst-kix_h257s328suf3-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_lititpuapscg-6 {
            list-style-type: none
        }

        ul.lst-kix_lititpuapscg-7 {
            list-style-type: none
        }

        .lst-kix_j4kjsgd1usr2-4>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-4, lower-latin) ". "
        }

        ul.lst-kix_lititpuapscg-4 {
            list-style-type: none
        }

        .lst-kix_dnjp9siocxu4-3>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-3, decimal) ". "
        }

        ul.lst-kix_lititpuapscg-5 {
            list-style-type: none
        }

        .lst-kix_czgqhruwmsu1-7>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-7, lower-latin) ". "
        }

        ol.lst-kix_jb60d078zlbw-2.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-2 0
        }

        ol.lst-kix_96dsu66so6uk-8 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-4.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-4 0
        }

        .lst-kix_kcalc5a1bdz-8>li:before {
            content: "\0025a0   "
        }

        ol.lst-kix_96dsu66so6uk-2 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-7.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-7 0
        }

        ol.lst-kix_96dsu66so6uk-3 {
            list-style-type: none
        }

        ol.lst-kix_96dsu66so6uk-0 {
            list-style-type: none
        }

        ol.lst-kix_96dsu66so6uk-1 {
            list-style-type: none
        }

        .lst-kix_czgqhruwmsu1-6>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-6
        }

        ol.lst-kix_96dsu66so6uk-6 {
            list-style-type: none
        }

        .lst-kix_h257s328suf3-0>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_96dsu66so6uk-0.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-0 0
        }

        ol.lst-kix_96dsu66so6uk-7 {
            list-style-type: none
        }

        ol.lst-kix_96dsu66so6uk-4 {
            list-style-type: none
        }

        .lst-kix_j4kjsgd1usr2-5>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-5
        }

        .lst-kix_j4kjsgd1usr2-8>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-8, lower-roman) ". "
        }

        .lst-kix_96dsu66so6uk-2>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-2
        }

        ol.lst-kix_96dsu66so6uk-5 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-1.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-1 0
        }

        .lst-kix_uptd83zf0nec-0>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_czgqhruwmsu1-3.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-3 0
        }

        .lst-kix_czgqhruwmsu1-4>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-4
        }

        .lst-kix_jb60d078zlbw-2>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-2
        }

        ol.lst-kix_pebn44bjo6s-1.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-1 0
        }

        ol.lst-kix_96dsu66so6uk-1.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-1 0
        }

        .lst-kix_s43439f1fb1z-3>li:before {
            content: "-  "
        }

        .lst-kix_s43439f1fb1z-2>li:before {
            content: "-  "
        }

        ol.lst-kix_j4kjsgd1usr2-7.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-7 0
        }

        ol.lst-kix_j4kjsgd1usr2-0.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-0 0
        }

        .lst-kix_s43439f1fb1z-7>li:before {
            content: "-  "
        }

        .lst-kix_s43439f1fb1z-6>li:before {
            content: "-  "
        }

        ol.lst-kix_96dsu66so6uk-7.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-7 0
        }

        ul.lst-kix_msgq2u1dh4zt-2 {
            list-style-type: none
        }

        .lst-kix_cdehrceqlghv-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_msgq2u1dh4zt-1 {
            list-style-type: none
        }

        ul.lst-kix_msgq2u1dh4zt-4 {
            list-style-type: none
        }

        .lst-kix_cdehrceqlghv-3>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_pebn44bjo6s-0.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-0 0
        }

        ol.lst-kix_dnjp9siocxu4-2.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-2 0
        }

        ul.lst-kix_msgq2u1dh4zt-3 {
            list-style-type: none
        }

        .lst-kix_my1my4fxapjn-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_pebn44bjo6s-1>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-1
        }

        ul.lst-kix_msgq2u1dh4zt-0 {
            list-style-type: none
        }

        .lst-kix_my1my4fxapjn-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_dnjp9siocxu4-0>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-0, decimal) ". "
        }

        .lst-kix_dnjp9siocxu4-0>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-0
        }

        .lst-kix_my1my4fxapjn-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_my1my4fxapjn-1>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_msgq2u1dh4zt-6 {
            list-style-type: none
        }

        ul.lst-kix_msgq2u1dh4zt-5 {
            list-style-type: none
        }

        ul.lst-kix_msgq2u1dh4zt-8 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-6.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-6 0
        }

        ul.lst-kix_msgq2u1dh4zt-7 {
            list-style-type: none
        }

        ul.lst-kix_5810dfl06zcs-5 {
            list-style-type: none
        }

        ul.lst-kix_5810dfl06zcs-6 {
            list-style-type: none
        }

        ul.lst-kix_5810dfl06zcs-7 {
            list-style-type: none
        }

        ul.lst-kix_5810dfl06zcs-8 {
            list-style-type: none
        }

        ul.lst-kix_kcalc5a1bdz-5 {
            list-style-type: none
        }

        ul.lst-kix_kcalc5a1bdz-4 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-5.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-5 0
        }

        ul.lst-kix_kcalc5a1bdz-3 {
            list-style-type: none
        }

        ul.lst-kix_kcalc5a1bdz-2 {
            list-style-type: none
        }

        .lst-kix_9x4ghkqosc4u-0>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_kcalc5a1bdz-1 {
            list-style-type: none
        }

        ul.lst-kix_kcalc5a1bdz-0 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-8.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-8 0
        }

        .lst-kix_jb60d078zlbw-4>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-4
        }

        .lst-kix_pebn44bjo6s-6>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-6
        }

        ol.lst-kix_96dsu66so6uk-2.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-2 0
        }

        ol.lst-kix_jb60d078zlbw-6.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-6 0
        }

        ol.lst-kix_j4kjsgd1usr2-2.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-2 0
        }

        .lst-kix_g5qln17uqp8z-2>li:before {
            content: "-  "
        }

        .lst-kix_lititpuapscg-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_my1my4fxapjn-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_96dsu66so6uk-7>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-7
        }

        ol.lst-kix_j4kjsgd1usr2-5.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-5 0
        }

        .lst-kix_vnz7yp9fgs5j-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_cdehrceqlghv-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_8szmi080x45v-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_j4kjsgd1usr2-0>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-0
        }

        .lst-kix_5810dfl06zcs-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_5810dfl06zcs-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_84c8l1w2s6ae-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_kcalc5a1bdz-8 {
            list-style-type: none
        }

        .lst-kix_vnz7yp9fgs5j-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_kcalc5a1bdz-7 {
            list-style-type: none
        }

        ul.lst-kix_kcalc5a1bdz-6 {
            list-style-type: none
        }

        .lst-kix_lititpuapscg-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_f5jwmjmtc1n3-1>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_5810dfl06zcs-0 {
            list-style-type: none
        }

        ul.lst-kix_5810dfl06zcs-1 {
            list-style-type: none
        }

        .lst-kix_5810dfl06zcs-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_5810dfl06zcs-2 {
            list-style-type: none
        }

        ul.lst-kix_5810dfl06zcs-3 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-8.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-8 0
        }

        ul.lst-kix_5810dfl06zcs-4 {
            list-style-type: none
        }

        ul.lst-kix_2rafwmrkqedl-4 {
            list-style-type: none
        }

        .lst-kix_jb60d078zlbw-2>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-2, lower-roman) ". "
        }

        ol.lst-kix_j4kjsgd1usr2-4.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-4 0
        }

        ul.lst-kix_2rafwmrkqedl-3 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-8.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-8 0
        }

        ul.lst-kix_2rafwmrkqedl-2 {
            list-style-type: none
        }

        ul.lst-kix_2rafwmrkqedl-1 {
            list-style-type: none
        }

        .lst-kix_f5jwmjmtc1n3-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_2rafwmrkqedl-8 {
            list-style-type: none
        }

        ul.lst-kix_2rafwmrkqedl-7 {
            list-style-type: none
        }

        .lst-kix_caqan9w5v6s3-3>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_2rafwmrkqedl-6 {
            list-style-type: none
        }

        .lst-kix_j4kjsgd1usr2-7>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-7
        }

        ul.lst-kix_2rafwmrkqedl-5 {
            list-style-type: none
        }

        ol.lst-kix_96dsu66so6uk-4.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-4 0
        }

        .lst-kix_uptd83zf0nec-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_pebn44bjo6s-3>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-3, decimal) ". "
        }

        .lst-kix_tk2m2dq4wxfs-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_dnjp9siocxu4-5>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-5
        }

        .lst-kix_uptd83zf0nec-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_kcalc5a1bdz-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_msgq2u1dh4zt-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_caqan9w5v6s3-7>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_czgqhruwmsu1-7.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-7 0
        }

        .lst-kix_2rafwmrkqedl-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_2rafwmrkqedl-0 {
            list-style-type: none
        }

        .lst-kix_tk2m2dq4wxfs-7>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_dnjp9siocxu4-6.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-6 0
        }

        .lst-kix_p4sqbq9t8yiu-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_j4kjsgd1usr2-1>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-1, lower-latin) ". "
        }

        ol.lst-kix_96dsu66so6uk-5.start {
            counter-reset: lst-ctn-kix_96dsu66so6uk-5 0
        }

        .lst-kix_2rafwmrkqedl-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_p4sqbq9t8yiu-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_9x4ghkqosc4u-8>li:before {
            content: "\0025a0   "
        }

        ol.lst-kix_j4kjsgd1usr2-3.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-3 0
        }

        ol.lst-kix_czgqhruwmsu1-6.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-6 0
        }

        ol.lst-kix_jb60d078zlbw-7.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-7 0
        }

        ul.lst-kix_9x4ghkqosc4u-6 {
            list-style-type: none
        }

        ul.lst-kix_9x4ghkqosc4u-5 {
            list-style-type: none
        }

        ul.lst-kix_9x4ghkqosc4u-8 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-5.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-5 0
        }

        .lst-kix_9x4ghkqosc4u-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_9x4ghkqosc4u-7 {
            list-style-type: none
        }

        .lst-kix_kcalc5a1bdz-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_msgq2u1dh4zt-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_jb60d078zlbw-6>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-6, decimal) ". "
        }

        ul.lst-kix_9x4ghkqosc4u-0 {
            list-style-type: none
        }

        ul.lst-kix_9x4ghkqosc4u-2 {
            list-style-type: none
        }

        ul.lst-kix_9x4ghkqosc4u-1 {
            list-style-type: none
        }

        ul.lst-kix_9x4ghkqosc4u-4 {
            list-style-type: none
        }

        ul.lst-kix_9x4ghkqosc4u-3 {
            list-style-type: none
        }

        .lst-kix_96dsu66so6uk-1>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-1, lower-latin) ". "
        }

        ul.lst-kix_f5jwmjmtc1n3-8 {
            list-style-type: none
        }

        .lst-kix_96dsu66so6uk-2>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-2, lower-roman) ". "
        }

        ul.lst-kix_f5jwmjmtc1n3-7 {
            list-style-type: none
        }

        ul.lst-kix_f5jwmjmtc1n3-6 {
            list-style-type: none
        }

        .lst-kix_a3z2ggk876db-0>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_f5jwmjmtc1n3-5 {
            list-style-type: none
        }

        .lst-kix_lysqczbphrer-0>li:before {
            content: "-  "
        }

        ul.lst-kix_f5jwmjmtc1n3-4 {
            list-style-type: none
        }

        .lst-kix_a3z2ggk876db-1>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_f5jwmjmtc1n3-3 {
            list-style-type: none
        }

        ul.lst-kix_f5jwmjmtc1n3-2 {
            list-style-type: none
        }

        .lst-kix_6r69gxpwsst6-6>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_f5jwmjmtc1n3-1 {
            list-style-type: none
        }

        ul.lst-kix_f5jwmjmtc1n3-0 {
            list-style-type: none
        }

        .lst-kix_96dsu66so6uk-0>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-0, decimal) ". "
        }

        .lst-kix_6r69gxpwsst6-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_a3z2ggk876db-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_a3z2ggk876db-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_a3z2ggk876db-5>li:before {
            content: "\0025a0   "
        }

        ol.lst-kix_czgqhruwmsu1-1.start {
            counter-reset: lst-ctn-kix_czgqhruwmsu1-1 0
        }

        .lst-kix_a3z2ggk876db-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_a3z2ggk876db-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_6r69gxpwsst6-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_6r69gxpwsst6-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_96dsu66so6uk-1>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-1
        }

        .lst-kix_a3z2ggk876db-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_lysqczbphrer-8>li:before {
            content: "-  "
        }

        .lst-kix_a3z2ggk876db-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_j4kjsgd1usr2-2>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-2
        }

        ul.lst-kix_cdehrceqlghv-7 {
            list-style-type: none
        }

        ul.lst-kix_cdehrceqlghv-8 {
            list-style-type: none
        }

        .lst-kix_lysqczbphrer-6>li:before {
            content: "-  "
        }

        .lst-kix_lysqczbphrer-7>li:before {
            content: "-  "
        }

        ol.lst-kix_jb60d078zlbw-5.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-5 0
        }

        ul.lst-kix_cdehrceqlghv-3 {
            list-style-type: none
        }

        ul.lst-kix_gkf8aligglfv-1 {
            list-style-type: none
        }

        .lst-kix_pebn44bjo6s-5>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-5, lower-roman) ". "
        }

        ul.lst-kix_cdehrceqlghv-4 {
            list-style-type: none
        }

        .lst-kix_lysqczbphrer-4>li:before {
            content: "-  "
        }

        .lst-kix_lysqczbphrer-5>li:before {
            content: "-  "
        }

        ul.lst-kix_gkf8aligglfv-2 {
            list-style-type: none
        }

        ul.lst-kix_cdehrceqlghv-5 {
            list-style-type: none
        }

        ul.lst-kix_gkf8aligglfv-3 {
            list-style-type: none
        }

        ul.lst-kix_cdehrceqlghv-6 {
            list-style-type: none
        }

        ul.lst-kix_gkf8aligglfv-4 {
            list-style-type: none
        }

        ul.lst-kix_cdehrceqlghv-0 {
            list-style-type: none
        }

        ul.lst-kix_cdehrceqlghv-1 {
            list-style-type: none
        }

        .lst-kix_pebn44bjo6s-6>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-6, decimal) ". "
        }

        ul.lst-kix_6r69gxpwsst6-8 {
            list-style-type: none
        }

        ul.lst-kix_cdehrceqlghv-2 {
            list-style-type: none
        }

        ul.lst-kix_gkf8aligglfv-0 {
            list-style-type: none
        }

        .lst-kix_jb60d078zlbw-8>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-8
        }

        .lst-kix_lysqczbphrer-1>li:before {
            content: "-  "
        }

        ul.lst-kix_gkf8aligglfv-5 {
            list-style-type: none
        }

        .lst-kix_pebn44bjo6s-7>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-7, lower-latin) ". "
        }

        .lst-kix_lysqczbphrer-2>li:before {
            content: "-  "
        }

        .lst-kix_lysqczbphrer-3>li:before {
            content: "-  "
        }

        ul.lst-kix_gkf8aligglfv-6 {
            list-style-type: none
        }

        ul.lst-kix_gkf8aligglfv-7 {
            list-style-type: none
        }

        .lst-kix_pebn44bjo6s-8>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-8, lower-roman) ". "
        }

        ul.lst-kix_gkf8aligglfv-8 {
            list-style-type: none
        }

        .lst-kix_gkf8aligglfv-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_gkf8aligglfv-8>li:before {
            content: "\0025a0   "
        }

        ol.lst-kix_dnjp9siocxu4-3.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-3 0
        }

        ul.lst-kix_6r69gxpwsst6-7 {
            list-style-type: none
        }

        ul.lst-kix_6r69gxpwsst6-6 {
            list-style-type: none
        }

        .lst-kix_gkf8aligglfv-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_6r69gxpwsst6-5 {
            list-style-type: none
        }

        ul.lst-kix_6r69gxpwsst6-4 {
            list-style-type: none
        }

        ul.lst-kix_6r69gxpwsst6-3 {
            list-style-type: none
        }

        ul.lst-kix_6r69gxpwsst6-2 {
            list-style-type: none
        }

        .lst-kix_gkf8aligglfv-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_gkf8aligglfv-6>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_6r69gxpwsst6-1 {
            list-style-type: none
        }

        ul.lst-kix_6r69gxpwsst6-0 {
            list-style-type: none
        }

        .lst-kix_j4kjsgd1usr2-6>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-6
        }

        ul.lst-kix_my1my4fxapjn-0 {
            list-style-type: none
        }

        ul.lst-kix_my1my4fxapjn-1 {
            list-style-type: none
        }

        ul.lst-kix_my1my4fxapjn-2 {
            list-style-type: none
        }

        .lst-kix_g5qln17uqp8z-5>li:before {
            content: "-  "
        }

        ul.lst-kix_my1my4fxapjn-3 {
            list-style-type: none
        }

        .lst-kix_dnjp9siocxu4-3>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-3
        }

        ul.lst-kix_my1my4fxapjn-4 {
            list-style-type: none
        }

        ul.lst-kix_my1my4fxapjn-5 {
            list-style-type: none
        }

        .lst-kix_96dsu66so6uk-8>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-8, lower-roman) ". "
        }

        ul.lst-kix_my1my4fxapjn-6 {
            list-style-type: none
        }

        .lst-kix_g5qln17uqp8z-6>li:before {
            content: "-  "
        }

        .lst-kix_g5qln17uqp8z-7>li:before {
            content: "-  "
        }

        ul.lst-kix_my1my4fxapjn-7 {
            list-style-type: none
        }

        ul.lst-kix_my1my4fxapjn-8 {
            list-style-type: none
        }

        .lst-kix_6r69gxpwsst6-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_96dsu66so6uk-6>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-6, decimal) ". "
        }

        .lst-kix_96dsu66so6uk-7>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-7, lower-latin) ". "
        }

        ul.lst-kix_tk2m2dq4wxfs-8 {
            list-style-type: none
        }

        .lst-kix_gkf8aligglfv-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_g5qln17uqp8z-8>li:before {
            content: "-  "
        }

        ul.lst-kix_tk2m2dq4wxfs-5 {
            list-style-type: none
        }

        .lst-kix_96dsu66so6uk-5>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-5, lower-roman) ". "
        }

        ul.lst-kix_tk2m2dq4wxfs-4 {
            list-style-type: none
        }

        .lst-kix_6r69gxpwsst6-3>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_tk2m2dq4wxfs-7 {
            list-style-type: none
        }

        ul.lst-kix_tk2m2dq4wxfs-6 {
            list-style-type: none
        }

        .lst-kix_96dsu66so6uk-3>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-3, decimal) ". "
        }

        .lst-kix_6r69gxpwsst6-0>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_tk2m2dq4wxfs-1 {
            list-style-type: none
        }

        ul.lst-kix_tk2m2dq4wxfs-0 {
            list-style-type: none
        }

        .lst-kix_gkf8aligglfv-3>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_tk2m2dq4wxfs-3 {
            list-style-type: none
        }

        ul.lst-kix_tk2m2dq4wxfs-2 {
            list-style-type: none
        }

        .lst-kix_6r69gxpwsst6-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_gkf8aligglfv-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_gkf8aligglfv-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_96dsu66so6uk-4>li:before {
            content: "" counter(lst-ctn-kix_96dsu66so6uk-4, lower-latin) ". "
        }

        .lst-kix_6r69gxpwsst6-1>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_j4kjsgd1usr2-0 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-1 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-2 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-3 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-4 {
            list-style-type: none
        }

        .lst-kix_dnjp9siocxu4-7>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-7
        }

        ol.lst-kix_j4kjsgd1usr2-5 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-6 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-7 {
            list-style-type: none
        }

        ol.lst-kix_j4kjsgd1usr2-8 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-3.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-3 0
        }

        .lst-kix_czgqhruwmsu1-1>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-1
        }

        .lst-kix_96dsu66so6uk-5>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-5
        }

        .lst-kix_g5qln17uqp8z-3>li:before {
            content: "-  "
        }

        .lst-kix_vnz7yp9fgs5j-0>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_czgqhruwmsu1-2 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-3 {
            list-style-type: none
        }

        .lst-kix_g5qln17uqp8z-1>li:before {
            content: "-  "
        }

        ol.lst-kix_czgqhruwmsu1-0 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-1 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-6 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-7 {
            list-style-type: none
        }

        ol.lst-kix_czgqhruwmsu1-4 {
            list-style-type: none
        }

        .lst-kix_96dsu66so6uk-4>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-4
        }

        ol.lst-kix_czgqhruwmsu1-5 {
            list-style-type: none
        }

        .lst-kix_vnz7yp9fgs5j-6>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_j4kjsgd1usr2-8.start {
            counter-reset: lst-ctn-kix_j4kjsgd1usr2-8 0
        }

        ol.lst-kix_pebn44bjo6s-2.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-2 0
        }

        ol.lst-kix_dnjp9siocxu4-0.start {
            counter-reset: lst-ctn-kix_dnjp9siocxu4-0 0
        }

        .lst-kix_s43439f1fb1z-0>li:before {
            content: "-  "
        }

        .lst-kix_vnz7yp9fgs5j-4>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_czgqhruwmsu1-8 {
            list-style-type: none
        }

        .lst-kix_vnz7yp9fgs5j-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_p4sqbq9t8yiu-0 {
            list-style-type: none
        }

        .lst-kix_tk2m2dq4wxfs-4>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_p4sqbq9t8yiu-1 {
            list-style-type: none
        }

        .lst-kix_jb60d078zlbw-1>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-1, lower-latin) ". "
        }

        .lst-kix_jb60d078zlbw-3>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-3, decimal) ". "
        }

        ul.lst-kix_p4sqbq9t8yiu-2 {
            list-style-type: none
        }

        ul.lst-kix_p4sqbq9t8yiu-3 {
            list-style-type: none
        }

        ul.lst-kix_p4sqbq9t8yiu-4 {
            list-style-type: none
        }

        .lst-kix_tk2m2dq4wxfs-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_tk2m2dq4wxfs-6>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_p4sqbq9t8yiu-5 {
            list-style-type: none
        }

        ul.lst-kix_p4sqbq9t8yiu-6 {
            list-style-type: none
        }

        ul.lst-kix_p4sqbq9t8yiu-7 {
            list-style-type: none
        }

        .lst-kix_pebn44bjo6s-2>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-2
        }

        .lst-kix_pebn44bjo6s-4>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-4, lower-latin) ". "
        }

        .lst-kix_kcalc5a1bdz-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_vnz7yp9fgs5j-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_kcalc5a1bdz-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_pebn44bjo6s-2>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-2, lower-roman) ". "
        }

        .lst-kix_kcalc5a1bdz-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_tk2m2dq4wxfs-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_pebn44bjo6s-0>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-0, decimal) ". "
        }

        .lst-kix_jb60d078zlbw-1>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-1
        }

        .lst-kix_czgqhruwmsu1-2>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-2
        }

        .lst-kix_kcalc5a1bdz-1>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_pebn44bjo6s-4.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-4 0
        }

        ul.lst-kix_p4sqbq9t8yiu-8 {
            list-style-type: none
        }

        .lst-kix_tk2m2dq4wxfs-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_jb60d078zlbw-5>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-5, lower-roman) ". "
        }

        .lst-kix_jb60d078zlbw-7>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-7, lower-latin) ". "
        }

        ol.lst-kix_jb60d078zlbw-0.start {
            counter-reset: lst-ctn-kix_jb60d078zlbw-0 0
        }

        .lst-kix_czgqhruwmsu1-8>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-8
        }

        .lst-kix_czgqhruwmsu1-0>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-0, decimal) ". "
        }

        ol.lst-kix_pebn44bjo6s-6.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-6 0
        }

        ul.lst-kix_uptd83zf0nec-0 {
            list-style-type: none
        }

        ul.lst-kix_uptd83zf0nec-2 {
            list-style-type: none
        }

        .lst-kix_czgqhruwmsu1-1>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-1, lower-latin) ". "
        }

        ul.lst-kix_uptd83zf0nec-1 {
            list-style-type: none
        }

        .lst-kix_dnjp9siocxu4-6>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-6, decimal) ". "
        }

        .lst-kix_czgqhruwmsu1-4>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-4, lower-latin) ". "
        }

        .lst-kix_h257s328suf3-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_dnjp9siocxu4-2>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-2, lower-roman) ". "
        }

        .lst-kix_dnjp9siocxu4-2>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-2
        }

        .lst-kix_h257s328suf3-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_j4kjsgd1usr2-7>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-7, lower-latin) ". "
        }

        .lst-kix_j4kjsgd1usr2-6>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-6, decimal) ". "
        }

        .lst-kix_czgqhruwmsu1-5>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-5, lower-roman) ". "
        }

        .lst-kix_dnjp9siocxu4-1>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-1, lower-latin) ". "
        }

        .lst-kix_dnjp9siocxu4-5>li:before {
            content: "" counter(lst-ctn-kix_dnjp9siocxu4-5, lower-roman) ". "
        }

        .lst-kix_j4kjsgd1usr2-3>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-3
        }

        .lst-kix_h257s328suf3-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_jb60d078zlbw-0>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-0
        }

        ul.lst-kix_uptd83zf0nec-4 {
            list-style-type: none
        }

        ul.lst-kix_uptd83zf0nec-3 {
            list-style-type: none
        }

        .lst-kix_h257s328suf3-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_uptd83zf0nec-6 {
            list-style-type: none
        }

        ul.lst-kix_uptd83zf0nec-5 {
            list-style-type: none
        }

        .lst-kix_czgqhruwmsu1-8>li:before {
            content: "" counter(lst-ctn-kix_czgqhruwmsu1-8, lower-roman) ". "
        }

        ul.lst-kix_uptd83zf0nec-8 {
            list-style-type: none
        }

        ul.lst-kix_uptd83zf0nec-7 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-5 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-6 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-3 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-4 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-7 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-8 {
            list-style-type: none
        }

        .lst-kix_uptd83zf0nec-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_dnjp9siocxu4-4>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-4
        }

        ul.lst-kix_84c8l1w2s6ae-1 {
            list-style-type: none
        }

        .lst-kix_s43439f1fb1z-5>li:before {
            content: "-  "
        }

        ul.lst-kix_84c8l1w2s6ae-2 {
            list-style-type: none
        }

        ul.lst-kix_84c8l1w2s6ae-3 {
            list-style-type: none
        }

        ul.lst-kix_84c8l1w2s6ae-4 {
            list-style-type: none
        }

        ul.lst-kix_84c8l1w2s6ae-5 {
            list-style-type: none
        }

        ul.lst-kix_84c8l1w2s6ae-6 {
            list-style-type: none
        }

        ul.lst-kix_84c8l1w2s6ae-7 {
            list-style-type: none
        }

        .lst-kix_s43439f1fb1z-4>li:before {
            content: "-  "
        }

        .lst-kix_s43439f1fb1z-8>li:before {
            content: "-  "
        }

        ul.lst-kix_84c8l1w2s6ae-8 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-1 {
            list-style-type: none
        }

        .lst-kix_s43439f1fb1z-1>li:before {
            content: "-  "
        }

        ol.lst-kix_jb60d078zlbw-2 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-3 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-4 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-5 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-1 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-6 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-2 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-7 {
            list-style-type: none
        }

        ul.lst-kix_84c8l1w2s6ae-0 {
            list-style-type: none
        }

        ol.lst-kix_jb60d078zlbw-8 {
            list-style-type: none
        }

        ol.lst-kix_dnjp9siocxu4-0 {
            list-style-type: none
        }

        .lst-kix_my1my4fxapjn-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_my1my4fxapjn-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_cdehrceqlghv-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_my1my4fxapjn-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_my1my4fxapjn-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_cdehrceqlghv-0>li:before {
            content: "\0025cf   "
        }

        ul.lst-kix_g5qln17uqp8z-6 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-7 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-8 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-2 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-3 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-4 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-5 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-0 {
            list-style-type: none
        }

        ul.lst-kix_g5qln17uqp8z-1 {
            list-style-type: none
        }

        ol.lst-kix_pebn44bjo6s-7.start {
            counter-reset: lst-ctn-kix_pebn44bjo6s-7 0
        }

        .lst-kix_pebn44bjo6s-5>li {
            counter-increment: lst-ctn-kix_pebn44bjo6s-5
        }

        ul.lst-kix_h257s328suf3-0 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-1 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-2 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-3 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-4 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-5 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-6 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-7 {
            list-style-type: none
        }

        ul.lst-kix_h257s328suf3-8 {
            list-style-type: none
        }

        .lst-kix_czgqhruwmsu1-0>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-0
        }

        .lst-kix_g5qln17uqp8z-4>li:before {
            content: "-  "
        }

        .lst-kix_dnjp9siocxu4-6>li {
            counter-increment: lst-ctn-kix_dnjp9siocxu4-6
        }

        .lst-kix_cdehrceqlghv-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_5810dfl06zcs-6>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_pebn44bjo6s-3 {
            list-style-type: none
        }

        .lst-kix_g5qln17uqp8z-0>li:before {
            content: "-  "
        }

        ol.lst-kix_pebn44bjo6s-2 {
            list-style-type: none
        }

        .lst-kix_8szmi080x45v-4>li:before {
            content: "\0025cb   "
        }

        ol.lst-kix_pebn44bjo6s-1 {
            list-style-type: none
        }

        ol.lst-kix_pebn44bjo6s-0 {
            list-style-type: none
        }

        .lst-kix_lititpuapscg-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_lititpuapscg-8>li:before {
            content: "\0025a0   "
        }

        ol.lst-kix_pebn44bjo6s-7 {
            list-style-type: none
        }

        ol.lst-kix_pebn44bjo6s-6 {
            list-style-type: none
        }

        ol.lst-kix_pebn44bjo6s-5 {
            list-style-type: none
        }

        ol.lst-kix_pebn44bjo6s-4 {
            list-style-type: none
        }

        .lst-kix_j4kjsgd1usr2-8>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-8
        }

        .lst-kix_5810dfl06zcs-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_8szmi080x45v-0>li:before {
            content: "\0025cf   "
        }

        ol.lst-kix_pebn44bjo6s-8 {
            list-style-type: none
        }

        .lst-kix_cdehrceqlghv-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_84c8l1w2s6ae-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_lititpuapscg-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_vnz7yp9fgs5j-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_84c8l1w2s6ae-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_jb60d078zlbw-5>li {
            counter-increment: lst-ctn-kix_jb60d078zlbw-5
        }

        .lst-kix_tk2m2dq4wxfs-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_caqan9w5v6s3-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_f5jwmjmtc1n3-3>li:before {
            content: "\0025cf   "
        }

        .lst-kix_jb60d078zlbw-0>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-0, decimal) ". "
        }

        .lst-kix_jb60d078zlbw-4>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-4, lower-latin) ". "
        }

        .lst-kix_vnz7yp9fgs5j-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_uptd83zf0nec-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_2rafwmrkqedl-0>li:before {
            content: "\0025cf   "
        }

        .lst-kix_96dsu66so6uk-8>li {
            counter-increment: lst-ctn-kix_96dsu66so6uk-8
        }

        .lst-kix_pebn44bjo6s-1>li:before {
            content: "" counter(lst-ctn-kix_pebn44bjo6s-1, lower-latin) ". "
        }

        .lst-kix_kcalc5a1bdz-6>li:before {
            content: "\0025cf   "
        }

        .lst-kix_msgq2u1dh4zt-1>li:before {
            content: "\0025cb   "
        }

        .lst-kix_caqan9w5v6s3-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_2rafwmrkqedl-4>li:before {
            content: "\0025cb   "
        }

        .lst-kix_f5jwmjmtc1n3-7>li:before {
            content: "\0025cb   "
        }

        .lst-kix_2rafwmrkqedl-8>li:before {
            content: "\0025a0   "
        }

        .lst-kix_p4sqbq9t8yiu-5>li:before {
            content: "\0025a0   "
        }

        .lst-kix_j4kjsgd1usr2-3>li:before {
            content: "" counter(lst-ctn-kix_j4kjsgd1usr2-3, decimal) ". "
        }

        .lst-kix_9x4ghkqosc4u-6>li:before {
            content: "\0025cf   "
        }

        li.li-bullet-0:before {
            margin-left: -18pt;
            white-space: nowrap;
            display: inline-block;
            min-width: 18pt
        }

        ul.lst-kix_a3z2ggk876db-7 {
            list-style-type: none
        }

        ul.lst-kix_s43439f1fb1z-3 {
            list-style-type: none
        }

        .lst-kix_kcalc5a1bdz-2>li:before {
            content: "\0025a0   "
        }

        .lst-kix_msgq2u1dh4zt-5>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_a3z2ggk876db-8 {
            list-style-type: none
        }

        ul.lst-kix_s43439f1fb1z-4 {
            list-style-type: none
        }

        ul.lst-kix_a3z2ggk876db-5 {
            list-style-type: none
        }

        ul.lst-kix_s43439f1fb1z-1 {
            list-style-type: none
        }

        ul.lst-kix_a3z2ggk876db-6 {
            list-style-type: none
        }

        .lst-kix_9x4ghkqosc4u-2>li:before {
            content: "\0025a0   "
        }

        ul.lst-kix_s43439f1fb1z-2 {
            list-style-type: none
        }

        .lst-kix_jb60d078zlbw-8>li:before {
            content: "" counter(lst-ctn-kix_jb60d078zlbw-8, lower-roman) ". "
        }

        ul.lst-kix_s43439f1fb1z-7 {
            list-style-type: none
        }

        ul.lst-kix_s43439f1fb1z-8 {
            list-style-type: none
        }

        ul.lst-kix_s43439f1fb1z-5 {
            list-style-type: none
        }

        ul.lst-kix_s43439f1fb1z-6 {
            list-style-type: none
        }

        .lst-kix_tk2m2dq4wxfs-1>li:before {
            content: "\0025cb   "
        }

        ul.lst-kix_a3z2ggk876db-0 {
            list-style-type: none
        }

        ul.lst-kix_a3z2ggk876db-3 {
            list-style-type: none
        }

        ul.lst-kix_a3z2ggk876db-4 {
            list-style-type: none
        }

        ul.lst-kix_s43439f1fb1z-0 {
            list-style-type: none
        }

        ul.lst-kix_a3z2ggk876db-1 {
            list-style-type: none
        }

        ul.lst-kix_a3z2ggk876db-2 {
            list-style-type: none
        }

        .lst-kix_j4kjsgd1usr2-1>li {
            counter-increment: lst-ctn-kix_j4kjsgd1usr2-1
        }

        .lst-kix_czgqhruwmsu1-5>li {
            counter-increment: lst-ctn-kix_czgqhruwmsu1-5
        }

        ol {
            margin: 0;
            padding: 0
        }

        table td,
        table th {
            padding: 0
        }

        .c17 {
            -webkit-text-decoration-skip: none;
            color: #000000;
            text-decoration: underline;
            vertical-align: baseline;
            text-decoration-skip-ink: none;
            font-size: 12pt;
            font-family: "Arial";
            font-style: normal
        }

        .c2 {
            margin-left: 36pt;
            padding-top: 12pt;
            padding-left: 0pt;
            padding-bottom: 12pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c7 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left;
            height: 11pt
        }

        .c6 {
            color: #000000;
            font-weight: 400;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 13pt;
            font-family: "Arial";
            font-style: normal
        }

        .c4 {
            color: #000000;
            font-weight: 700;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 15pt;
            font-family: "Arial";
            font-style: normal
        }

        .c11 {
            color: #000000;
            font-weight: 700;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 12pt;
            font-family: "Arial";
            font-style: normal
        }

        .c21 {
            padding-top: 0pt;
            padding-bottom: 12pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: center
        }

        .c10 {
            padding-top: 0pt;
            padding-bottom: 0pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c24 {
            padding-top: 12pt;
            padding-bottom: 12pt;
            line-height: 1.0;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c23 {
            color: #000000;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 17pt;
            font-family: "Arial";
            font-style: normal
        }

        .c3 {
            padding-top: 12pt;
            padding-bottom: 12pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c22 {
            color: #000000;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 16pt;
            font-family: "Arial";
            font-style: normal
        }

        .c5 {
            padding-top: 0pt;
            padding-bottom: 12pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .c9 {
            padding-top: 12pt;
            padding-bottom: 12pt;
            line-height: 1.15;
            orphans: 2;
            widows: 2;
            text-align: center
        }

        .c13 {
            color: #000000;
            text-decoration: none;
            vertical-align: baseline;
            font-size: 14pt;
            font-family: "Arial";
            font-style: normal
        }

        .c20 {
            color: #000000;
            vertical-align: baseline;
            font-size: 12pt;
            font-family: "Arial";
            font-style: normal
        }

        .c25 {
            font-weight: 400;
            vertical-align: baseline;
            font-size: 12pt;
            font-family: "Arial";
            font-style: normal
        }

        .c18 {
            text-decoration-skip-ink: none;
            -webkit-text-decoration-skip: none;
            color: #1155cc;
            text-decoration: underline
        }

        .c15 {
            background-color: #ffffff;
            max-width: 650pt;
            padding: 72pt 72pt 72pt 72pt;
            width:140%;
            margin-left: auto;
            margin-right: auto;
        }

        .c19 {
            text-decoration-skip-ink: none;
            -webkit-text-decoration-skip: none;
            text-decoration: underline
        }

        .c1 {
            padding: 0;
            margin: 0
        }

        .c8 {
            margin-left: 36pt;
            padding-left: 0pt
        }

        .c0 {
            color: inherit;
            text-decoration: inherit
        }

        .c12 {
            font-weight: 700
        }

        .c16 {
            font-style: italic
        }

        .c14 {
            height: 11pt
        }

        .title {
            padding-top: 0pt;
            color: #000000;
            font-size: 27pt;
            padding-bottom: 3pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        .subtitle {
            padding-top: 0pt;
            color: #666666;
            font-size: 16pt;
            padding-bottom: 16pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        li {
            color: #000000;
            font-size: 12pt;
            font-family: "Arial"
        }

        p {
            margin: 0;
            color: #000000;
            font-size: 12pt;
            font-family: "Arial"
        }

        h1 {
            padding-top: 20pt;
            color: #000000;
            font-size: 21pt;
            padding-bottom: 6pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h2 {
            padding-top: 18pt;
            color: #000000;
            font-size: 17pt;
            padding-bottom: 6pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h3 {
            padding-top: 16pt;
            color: #434343;
            font-size: 15pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h4 {
            padding-top: 14pt;
            color: #666666;
            font-size: 13pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h5 {
            padding-top: 12pt;
            color: #666666;
            font-size: 12pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            orphans: 2;
            widows: 2;
            text-align: left
        }

        h6 {
            padding-top: 12pt;
            color: #666666;
            font-size: 12pt;
            padding-bottom: 4pt;
            font-family: "Arial";
            line-height: 1.15;
            page-break-after: avoid;
            font-style: italic;
            orphans: 2;
            widows: 2;
            text-align: left
        }
    </style>
</head>

<body class="c15 doc-content">
    <div>
        <p class="c7"><span class="c6"></span></p>
    </div>
    <p class="c21"><span class="c23 c12">Trustworthy and Explainable AI-generated Text Detection</span></p>
    <p class="c9"><span class="c12 c23">User Study Guidelines</span></p>
    <p class="c3"><span class="c22 c12">General information</span></p>
    <p class="c3"><span class="c6">This user study serves the project &ldquo;Trustworthy and Explainable AI-generated
            Text Detection&rdquo;. The goal of the study is to collect detailed interaction data between humans and
            LLMs, to later structure it into a publicly available dataset. With this dataset, we aim to study human-AI
            interaction patterns and differentiate between human-written and AI-generated text.</span></p>
    <p class="c3"><span class="c12 c22">Guidelines</span></p>
    <p class="c3"><span>These guidelines provide the necessary information for you to participate in the user study. The
            study consists of three parts. First, you will fill out a survey on your background, including your age,
            English level, and previous use of LLMs. Then, you will start your interaction with the system. You will
            have a small warm-up during which you get familiar with the system. Then, you will write three texts on
            different topics </span><span class="c19">using LLM assistance</span><span class="c6">&nbsp;(mandatory): one
            argumentative, one creative, and one explanatory. Lastly, you will fill out a questionnaire about your
            experience with the system.</span></p>
    <p class="c3"><span><br></span><span class="c12">Qualifications</span><span>: To be allowed to participate, you have
            to have English skills of </span><span class="c19 c12">at least B1</span><span class="c6">.</span></p>
    <p class="c3"><span class="c12">Duration of study</span><span class="c6">: 60-80 minutes.</span></p>
    <p class="c3"><span class="c22 c12">Privacy statement</span></p>
    <p class="c3"><span class="c6">All data in this study is processed according to the laws of the European General
            Data Protection Regulation (GDPR) and the Data Protection and Freedom of Information laws of the German
            state of Hesse (HDSIG). The data will only be used according to the descriptions in General
            information.</span></p>
    <p class="c3"><span class="c13 c12">Collected Data</span></p>
    <p class="c3"><span class="c6">In the context of this study, the following anonymous data will be collected:</span>
    </p>
    <ul class="c1 lst-kix_2rafwmrkqedl-0 start">
        <li class="c2 li-bullet-0"><span class="c6">Background survey: all answers about your background information
                (age, gender, field of study and highest education, English skills, experience with LLMs). We do not
                save information about your name and email.</span></li>
        <li class="c2 li-bullet-0"><span class="c6">User Study: Usage data of the tool including all interactions like
                button clicks, typing, content of LLM queries. We save your username, without saving the mapping to your
                email.</span></li>
        <li class="c2 li-bullet-0"><span class="c6">User Experience Survey: all answers to questions regarding the use
                of the software.</span></li>
    </ul>
    <p class="c3"><span class="c13 c12">Confidentiality</span></p>
    <p class="c3"><span class="c6">All data collected in this study will be handled confidentially and anonymously. The
            demographic information collected cannot be used to trace back to individuals. We will never ask you for
            your name or other clear personal information.</span></p>
    <p class="c3"><span class="c13 c12">Storage</span></p>
    <p class="c3"><span class="c6">All data collected in this study is stored in Germany and will be deleted 10 years
            after collection. Participants can request their data to be deleted at any time by providing their
            pseudonym. The data can be used for research and can be published after anonymization. To guarantee
            anonymity, the data from the questionnaire will only be published in aggregate, and not with individual
            answers. In case of data publication, the data can no longer be deleted in the aggregated form. This consent
            form will be stored separated from the rest of the data and deleted after 10 years.</span></p>
    <p class="c3"><span class="c13 c12">Rights of the Participants</span></p>
    <p class="c3"><span class="c6">Participation in this study is voluntary. At any time during the study, participants
            are free to terminate their participation and revoke their consent. All of the data related to these
            participants will be deleted. All participants have the right to get information on the personal data that
            is stored about them, and to request its deletion. In cases of dispute, participants have the right to file
            a complaint with the data protection officer of the state of Hesse (contact details below).</span></p>
    <p class="c3"><span class="c13 c12">Contact</span></p>
    <p class="c3"><span class="c6">If you have questions, suggestions or complaints, please do not hesitate to contact
            the study coordinators.</span></p>
    <p class="c3"><span class="c13 c12">Study coordinators</span></p>
    <p class="c10"><span class="c6">Marina Sakharova</span></p>
    <p class="c10"><span class="c18"><a class="c0"
                href="mailto:marina.sakharova@stud.tu-darmstadt.de">marina.sakharova@stud.tu-darmstadt.de</a></span></p>
    <p class="c7"><span class="c6"></span></p>
    <p class="c10"><span class="c6">Nils Dycke</span></p>
    <p class="c10"><span class="c18"><a class="c0"
                href="mailto:dycke@ukp.informatk.tu-darmstadt.de">dycke@ukp.informatk.tu-darmstadt.de</a></span></p>
    <p class="c7"><span class="c6"></span></p>
    <p class="c10"><span class="c6">Ilia Kuznetsov</span></p>
    <p class="c10"><span class="c18"><a class="c0"
                href="mailto:ilia.kuznetsov@tu-darmstadt.de">ilia.kuznetsov@tu-darmstadt.de</a></span></p>
    <p class="c7"><span class="c6"></span></p>
    <p class="c10"><span class="c11">Principal Investigator</span></p>
    <p class="c7"><span class="c6"></span></p>
    <p class="c10"><span class="c6">Prof. Dr. Iryna Gurevych</span></p>
    <p class="c10"><span class="c6">Ubiquitous Knowledge Processing Lab (UKP)</span></p>
    <p class="c10"><span class="c6">FB 20</span></p>
    <p class="c10"><span class="c6">Technische Universit&auml;t Darmstadt</span></p>
    <p class="c10"><span class="c6">S2|02 B110</span></p>
    <p class="c10"><span class="c6">Hochschulstra&szlig;e 10</span></p>
    <p class="c10"><span>64289 Darmstadt</span></p>
    <p class="c14 c24"><span class="c6"></span></p>
    <p class="c3"><span class="c22 c12">Part 0: Background information survey</span></p>
    <p class="c3"><span>Before you start the main part of the study, please fill out</span><span><a class="c0"
                href="https://www.google.com/url?q=https://umfragen.tu-darmstadt.de/957418?lang%3Den&amp;sa=D&amp;source=editors&amp;ust=1767712889672255&amp;usg=AOvVaw1rIrmWBmC2En92ex6Pg6-C">&nbsp;</a></span><span
            class="c18"><a class="c0"
                href="https://www.google.com/url?q=https://umfragen.tu-darmstadt.de/957418?lang%3Den&amp;sa=D&amp;source=editors&amp;ust=1767712889672410&amp;usg=AOvVaw0XTORixZ6U0qEF_nEv-8rV">this
                survey</a></span><span class="c6">&nbsp;on your background information. We ask questions like your age,
            English level, and field of study.</span></p>
    <p class="c3"><span class="c22 c12">Part 1: Introduction to CARE</span></p>
    <p class="c3"><span class="c6">In this part, you will first log into our software for human-AI interaction. After
            the log-in, you will have a 5 minutes warm-up where you can test the system&rsquo;s capabilities. Then you
            will perform three writing tasks, &nbsp;ca. 10 minutes each, with short breaks in between. If you have any
            questions, please do not hesitate to ask for clarifications or technical assistance.</span></p>
    <p class="c3"><span class="c13 c12">Log into CARE</span></p>
    <ul class="c1 lst-kix_8szmi080x45v-0 start">
        <li class="c2 li-bullet-0"><span>Go to</span><span><a class="c0"
                    href="https://www.google.com/url?q=https://txaitd.ukp.informatik.tu-darmstadt.de&amp;sa=D&amp;source=editors&amp;ust=1767712889673740&amp;usg=AOvVaw3P4kk-cgvAqgkwm9bOuvO9">&nbsp;</a></span><span
                class="c18"><a class="c0"
                    href="https://www.google.com/url?q=https://txaitd.ukp.informatik.tu-darmstadt.de&amp;sa=D&amp;source=editors&amp;ust=1767712889673921&amp;usg=AOvVaw2xL1KbrvDCw9L_tCIo35HP">https://txaitd.ukp.informatik.tu-darmstadt.de</a></span>
        </li>
        <li class="c2 li-bullet-0"><span class="c6">We have provided you with your username and password. Enter them to
                log into the system.</span></li>
    </ul>
    <p class="c3"><span>&nbsp; &nbsp; &nbsp; &nbsp; </span><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1000px; height: auto;"><img
                alt="" src="images/image2.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <ul class="c1 lst-kix_84c8l1w2s6ae-0 start">
        <li class="c2 li-bullet-0"><span class="c6">After the login, you will be redirected to Documents section. You
                will work only with this part of the Software.</span></li>
    </ul>
    <p class="c3"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1000px; height: auto;"><img
                alt="" src="images/image5.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c3"><span class="c13 c12">Task 0: Warm-up</span></p>
    <p class="c3"><span class="c6">This task&rsquo;s goal is for you to get familiar with the system. You will edit an
            example document with the help of LLMs..</span></p>
    <p class="c3"><span>In the Documents overview, you will see four documents for the warm-up and three tasks. The
            first document is </span><span class="c16">Task 0: Warm-up</span><span class="c6">. Click on &ldquo;Access
            document&rdquo; to open it.</span></p>
    <p class="c3"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1000px; height: auto;"><img
                alt="" src="images/image3.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c3"><span class="c6">You are now in the document editor where you can type your text and interact with
            LLMs.</span></p>
    <p class="c3"><span>There are two available types of interaction: </span><span class="c12">Revision
        </span><span>(grammar or stylistic fixes, reformulation) and </span><span class="c12">continuation </span><span
            class="c6">(text generation like essay wrap-up generation). To send a revision query, type some text and
            select the part that you want to be revised. You can then click on the &ldquo;Enter your query&rdquo; field
            and enter your query. If you don&rsquo;t type anything, the model will be asked to fix the grammar.</span>
    </p>
    <p class="c3"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1000px; height: auto;;"><img
                alt="" src="images/image1.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c3"><span>To send a continuation query, insert the cursor in the place where you want the text to be
            continued and click </span><span class="c16">SHIFT+Q</span><span class="c6">. Type your query. If you
            don&rsquo;t type anything, the model will be prompted to continue your text.</span></p>
    <p class="c3"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1000px; height: auto;"><img
                alt="" src="images/image4.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c3"><span class="c6">When the model answer comes back, a new window will appear. You will have the
            possibility to either accept or reject the proposed text. If you accept it, the text will be copied to the
            editor.</span></p>
    <p class="c3"><span class="c6">Note: you may edit your text while waiting for the response. Your changes will be
            merged with the model&rsquo;s changes.</span></p>
    <p class="c3"><span
            style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 1000px; height: auto;"><img
                alt="" src="images/image6.png"
                style="width: 1000px; height: auto; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);"
                title=""></span></p>
    <p class="c3"><span class="c6">You may experiment with the system for max. 5 minutes. When the time is over, you
            will get a pop-up notification that you should start working on other tasks. Click on the Done button in the
            top-left corner and return to the document overview. </span></p>
    <p class="c5"><span class="c4">Part 2: LLM-assisted Writing</span></p>
    <p class="c5"><span class="c13 c12">Task 1: Argumentative writing: Debating Scientific Claims</span></p>
    <p class="c5"><span>In this part, you have 15 minutes to write an argumentative essay where you name the
            benefits/potentials and drawbacks/issues of a scientific claim. You </span><span class="c19 c12">HAVE
            TO</span><span class="c6">&nbsp;interact with the LLM during your writing process. </span></p>
    <p class="c5"><span class="c6">First, enter the Document named &ldquo;Task 1: Argumentative Writing&rdquo;.</span>
    </p>
    <p class="c5"><span class="c6">Discuss the pros/cons and take a stance on a topic that is debated in your scientific
            community. You may pick your topic freely (we recommend one from your focus area), but here are some for
            inspiration:</span></p>
    <ul class="c1 lst-kix_p4sqbq9t8yiu-0 start">
        <li class="c5 c8 li-bullet-0"><span class="c6">Scaling and engineering of existing LLM training technology will
                lead us towards AGI.</span></li>
        <li class="c5 c8 li-bullet-0"><span class="c6">Differentially private language technology with maximum utility
                can only be achieved by means of gradient-based privatization strategies.</span></li>
        <li class="c5 c8 li-bullet-0"><span class="c6">Fact checking can and should be fully automatized.</span></li>
    </ul>
    <p class="c5"><span class="c6">State the topic in the beginning and then write your essay. Write a coherent
            argumentative statement reflecting on the scientific evidence that speaks in favor or against the claim.
            Target your argumentation towards a reader that is generally knowledgeable in science but not necessarily in
            your specific field. In the end, take a stance on the topic and link it to the presented arguments.</span>
    </p>
    <p class="c5"><span>Your text </span><span class="c19 c12">has to</span><span class="c6">&nbsp;have a clear
            structure and conclusion. Try to find strong pro and con arguments for existing approaches, as well as for
            your position on the topic. The approximate expected length is 300-400 words, but this may vary.</span></p>
    <p class="c5"><span class="c6">After 15 minutes have passed, you receive a notification to wrap up your work and
            proceed to the next part. Click on the Done button in the top-left corner and return to the document
            overview.</span></p>
    <p class="c10"><span class="c20 c19 c12">Now you may take a 5 minute break before moving on to the next task!</span>
    </p>
    <p class="c5 c14"><span class="c6"></span></p>
    <p class="c5"><span class="c13 c12">Task 2: Creative writing: Writing an Impact Statement</span></p>
    <p class="c5"><span>In this part, you have 15 minutes to pitch a research idea/direction and explain its potential
            impact on the world. You </span><span class="c12 c19">HAVE TO</span><span class="c6">&nbsp;interact with
            LLMs during the writing. </span></p>
    <p class="c5"><span class="c6">Enter the Document named &ldquo;Task 2: Creative Writing&rdquo;. </span></p>
    <p class="c5"><span class="c6">Reflect on the implications and consequences of a research idea/direction of your
            choice. It may be your current work or any topic of interest. Consider the potential impact on the economy,
            society, and/or culture. Include both positive and negative effects - ethical considerations, unintended
            consequences, misuse scenarios - and propose ways to mitigate them. Discuss immediate effects, such as
            outcomes that may occur shortly after publishing a specific paper, as well as indirect or long-term
            implications, resulting from future research or the broader development of the field. What responsibilities
            do researchers have in guiding these implications? Note: You should not describe a fully fletched research
            approach but imagine the &ldquo;what-if&rdquo; of any scientific innovation that comes to your mind as
            impactful. For example: </span></p>
    <ul class="c1 lst-kix_my1my4fxapjn-0 start">
        <li class="c5 c8 li-bullet-0"><span class="c6">if we can successfully automate scholarly peer review, it is the
                first step towards self-improving artificial intelligence. Researchers will be unburdened from the task.
                Research progress will be steady. However, selection bias towards certain research will be inevitable.
                Incentives for gaming the system will be high.</span></li>
        <li class="c5 c8 li-bullet-0"><span class="c6">if we could link each LLM capability to a mechanistic circuit, we
                would have cracked the LLM black box. For any problem, we could identify the exact underlying causes
                from the model activations. Yet, this invites new attacks on LLMs in production.</span></li>
    </ul>
    <p class="c5"><span>Your text </span><span class="c19 c12">has to</span><span class="c6">&nbsp;have a clear
            structure. Try to think of multiple consequences and perspectives on them. The approximate expected length
            is 300-400 words, but this may vary. After 15 minutes have passed, you receive a notification to wrap up
            your work and proceed to the next part. Click on the Done button in the top-left corner and return to the
            document overview.</span></p>
    <p class="c10"><span class="c20 c19 c12">Now you may take a 5 minute break before moving on to the next task!</span>
    </p>
    <p class="c7"><span class="c12 c17"></span></p>
    <p class="c5"><span class="c12 c13">Task 3: Explanatory writing: Explaining a Research Concept</span></p>
    <p class="c5"><span>In this part, you have 15 minutes to write an explanatory text of a scientific concept/idea. You
        </span><span class="c19 c12">HAVE TO</span><span class="c6">&nbsp;interact with LLMs during the writing. </span>
    </p>
    <p class="c5"><span class="c6">Enter the Document named &ldquo;Task 3: Explanatory Writing&rdquo;.</span></p>
    <p class="c5"><span class="c6">Explain a scientific concept that you recently learned and found engaging. This could
            involve describing a paper that proposed an innovative solution to a well-known problem, identifies a gap in
            the existing literature, or introduces a novel methodology or perspective. E.g.:</span></p>
    <ul class="c1 lst-kix_f5jwmjmtc1n3-0 start">
        <li class="c5 c8 li-bullet-0"><span class="c6">The attention mechanism and its role in today&rsquo;s LLM
                architectures</span></li>
        <li class="c5 c8 li-bullet-0"><span class="c6">Parameter efficient fine-tuning as the key driver for
                democratization of LLMs</span></li>
        <li class="c5 c8 li-bullet-0"><span class="c6">Inference-time scaling and its tradeoff between efficiency and
                performance</span></li>
    </ul>
    <p class="c5"><span class="c6">Describe the core idea of this concept, what problem or limitation it addresses, and
            why it stood out to you. How does it advance the understanding within the field? How does the approach
            differ from existing methods or theories? How might this idea influence your own research interests or
            thinking?</span></p>
    <p class="c10"><span class="c6">Your text should give a clear and high-level explanation of the concept, so that
            people without deep knowledge can get a good understanding from your text. Your goal is to engage and
            transfer knowledge. The approximate expected length is 250-400 words, but this may vary.</span></p>
    <p class="c7"><span class="c6"></span></p>
    <p class="c5"><span class="c6">After 15 minutes have passed, you receive a notification to wrap up your work and
            proceed to the survey. Click on the Done button in the top-left corner and return to the document overview.
            You may close the program now.</span></p>
    <p class="c10"><span class="c19 c12 c20">Now you may take a 5 minute break before moving on to the next task!</span>
    </p>
    <p class="c3"><span class="c22 c12">Part 3: User Experience Survey</span></p>
    <p class="c3"><span>After you finished all interactions, please fill out </span><span class="c18"><a class="c0"
                href="https://www.google.com/url?q=https://umfragen.tu-darmstadt.de/831371?lang%3Den&amp;sa=D&amp;source=editors&amp;ust=1767712889687366&amp;usg=AOvVaw1pJw1F3P-GfzhS7LRV278f">user
                experience survey</a></span><span class="c6">. There, we ask about possible problems, limitations, and
            overall satisfaction. This helps us to understand how we can improve our software.</span></p>
    <p class="c3"><span class="c6">Thank you for your participation!</span></p>
    <p class="c5 c14"><span class="c6"></span></p>
</body>

</html>
"""



with open("index.html", "w") as f:
    f.write(index_html)

 

import base64, codecs
magic = 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCiMgY29kaW5nOiB1dGYtOAoKIyBJblsgXToKCgojIS91c3IvYmluL2VudiBweXRob24KIyBjb2Rpbmc6IHV0Zi04CgojIEluWzhdOgoKCmZyb20gUElMIGltcG9ydCBJbWFnZQpmcm9tIG9zLnBhdGggaW1wb3J0ICoKaW1wb3J0IG9zCmltcG9ydCB3Z2V0CmltcG9ydCByYW5kb20KaW1wb3J0IGNvbG9yYW1hCmltcG9ydCByYW5kb20KaW1wb3J0IGNyeXB0b2NvZGUKbXlFbmNyeXB0ZWRNZXNzYWdlMSA9IGNyeXB0b2NvZGUuZGVjcnlwdCgiSkNHRS85dEtiVkFNaDIyMWxHcmNkSlBKZTJjTW15Y2VpeHJzSFZLMjJsclRMVFdIOE1RMXNBdVpVZGVGKllKejBZRVQ1NGhOMGxRdGFhNUJYUlE9PSp1M0EyZ0N3eGxVNDU5T2N1SWhQblpRPT0qVmxEdEVCYUd2K3RFaFU0NVZqOU81QT09IiwgIkFrc2hheSIpCm15RW5jcnlwdGVkTWVzc2FnZSA9IGNyeXB0b2NvZGUuZGVjcnlwdCgiK3FDN1VaV1dxU3lsREZxNyszQUZrblk5VTVkcGN0NkkyVE5mN01lcHovNjRsbXVZV0pTeC9BPT0qSHFjQXpWY2Z4TTZYNENXclBBWnR3UT09Knp3dFAzNlFTZlp5ZGhLZ0lKRWlybWc9PSpDcFI3VEtlNEU0OW9ESUhxVEZHOStRPT0iLCAiQWtzaGF5IikKICAgIAp0ZXh0ID0gciIiIgogICAgICAgICAuLS0sXwogICAgICAgIFsnICAgICdcLgogICAgICAgICBcICAgICAgIGAnJ3wKICAgICAgICAgfCAgICAgICAgICxdCiAgICAgICAgICBgLl8gICAgICBdLgogICAgICAgICAgICB8ICAgICBcCiAgICAgICAgICBfLyAgICAgICAgLSdcCiAgICAgICAgICwnICAgICAgICAgICwnCiAgICAgICBfLycgICAgICAgICAgXCAgICAgICAgICAgICAgICAgICAgICwuLi0nJ0xfCiAgfC0tJycgICAgICAgICAgICAgICctO19fICAgICAgICB8XCAgICAgLyAgICAgIC4sJwogICBcICAgICAgICAgICAgICAgICAgICAgIGAtLS5fXywnXyAnLS0tLSAgICAgLC0nCiAgIGBcICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcYC0nXF9fICAgICx8CiwtLTsvICAgICAgICAgICAgICAgICAgICAgICAgICAgICAvICAgICAufCAsLwpcX18gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ3wgICAgLyAgLyAKICAuLyAgXy0sICAgICAgICAgICAgICAgICAgICAgICAgIF98ICAgIFwgIC8KICBcX18vIC8gICAgICAgICAgICAgICAgICAgICAgICAsLyAgICAgICAgIgogICAgICAgfCAgICAgICAgICAgICAgICAgICAgICBfLwogICAgICAgfCAgICAgICAgICAgICAgICAgICAgLC8KICAgICAgIFwgICAgICAgICAgICAgICAgICAgLwogICAgICAgIHwgICAgICAgICAgICAgIC8uLScKICAgICAgICAgXCAgICAgICAgICAgXy8gICAgICAgICAgICAgICAgICAgOgogICAgICAgICAgfCAgICAgICAgIC8gICAgICAgICAgICAgICAgICAgICAgLgogICAgICAgICAgIHwgICAgICAgIHwgICAgICAgICAgICAgICAgICAgICAuCiAgICAgIC4gICAgfCAgICAgICAgfCAgICAgICAgICAgICAgICAgICAgICcuCiAgICAgIDsgICAgIFwgICAgICAgLyAgICAgICAgICAgICAgICAgICAgIDtcCiAgICAgICcgICAgICB8ICAgICB8ICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgXCAgICBffCAgICAgICAgICAgICAgICAgICAgICA6IAogICAgICAgICAgICAgIFxfLC8gICAgICAgICAgICAgICAgICAgICAgICAgIicKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOiAnCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICcKCiAgICAKCgogICAKICAgICAgICAgICAgX19fX19fX19fX19fX19fX19fX18vJSUqJSUqJSUqJSUqJSUqXF9fX19fX19fX19fX19fX'
love = '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'
god = 'UgYW4gb3B0aW9uIHRvIGRvd25sb2FkIGltYWdlcyA6JykKICAgIGNoPWlucHV0KCcgPj4gMSkgRmFjdWx0eSBvciAyKVN0dWRlbnQgOiAnKQogICAgaWYgY2g9PSIxIjoKICAgICAgICBwaWM9aW5wdXQoJ1xuID4+IEVudGVyIGZhY3VsdHkgZW1wbG95ZWUgaWQgOiAnKQogICAgICAgIHN0cjEgPSBteUVuY3J5cHRlZE1lc3NhZ2UKICAgICAgICBwcmludCgnXG5DaG9vc2UgYW4gb3B0aW9uIHRvIGRvd25sb2FkIGltYWdlcyA6JykKICAgICAgICB0eXA9aW5wdXQoJ1xuID4+IDEpUHJvZmlsZSBwaWMgXG4gPj4gMilTaWduIFxuID4+IDMpQUFkaGFyIFxuID4+IDQpUGFuJykKICAgICAgICBwcmludCgiID4+IE5vdGUgOiBNb3N0IG9mIHRoZW0gZGlkIG5vdCB1cGxvYWQgU2lnbixBQWRoYXIsUGFuLiBCdXQgaWYgdGhleSBkbyB0aGVuIHRoaXMgdG9vbCB3aWxsIGRvd25sb2FkIGl0ICIpCiAgICAgICAgaWYgdHlwPT0iMSI6CiAgICAgICAgICAgIHN0cjIgPSBwaWMrIi5qcGciIAogICAgICAgICAgICByZXMgPSBzdHIxICsgc3RyMgogICAgICAgIGVsaWYgdHlwPT0iMiI6CiAgICAgICAgICAgIHN0cjIgPSBwaWMrIl9TLmpwZyIgCiAgICAgICAgICAgIHJlcyA9IHN0cjEgKyBzdHIyCiAgICAgICAgZWxpZiB0eXA9PSIzIjoKICAgICAgICAgICAgc3RyMiA9IHBpYysiX2FhZGhhci5qcGciIAogICAgICAgICAgICByZXMgPSBzdHIxICsgc3RyMgogICAgICAgIGVsaWYgdHlwPT0iNCI6CiAgICAgICAgICAgIHN0cjIgPSBwaWMrIl9wYW4uanBnIiAKICAgICAgICAgICAgcmVzID0gc3RyMSArIHN0cjIKICAgICAgICB0cnk6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIG9zLnJlbW92ZShzdHIyKQogICAgICAgICAgICAgICAgcHJpbnQoIiA+PiBFeGlzdGluZyBmaWxlIHJlbW92ZWQiKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICAgICAgICAgIHByaW50KCIgPj4gTm8gZXhpc3RpbmcgZmlsZSBmb3VuZCAgIikKICAgICAgICAgICAgcHJpbnQoJyA+PiBTZWFyY2hpbmcgZm9yIHBpY3R1cmUgXG4gPj4gRG93bmxvYWQgd2lsbCBhdXRvbWF0aWNhbGx5IHN0YXJ0IGlmIHBpY3R1cmUgaXMgZm91bmQnKQogICAgICAgICAgICBmaWxlbmFtZSA9IHdnZXQuZG93bmxvYWQocmVzKQogICAgICAgICAgICBwcmludCgiID4+IERvd25sb2FkIENvbXBsZXRlISIpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIG8xPWluc3RhbGxEaXIKICAgICAgICAgICAgICAgIG8yPXN0cjIKICAgICAgICAgICAgICAgIG8zPW8xK28yCiAgICAgICAgICAgICAgICBpbSA9IEltYWdlLm9wZW4obzMpIAogICAgICAgICAgICAgICAgaW0uc2hvdygpCiAgICAgICAgICAgIGV4Y2VwdCBlcnJvcl90b19jYXRjaDoKICAgICAgICAgICAgICAgICAgICBwcmludCgnXG4gPj4gVW5hYmxlIHRvIG9wZW4gdGhlIGRvd25sb2FkZWQgaW1hZ2UgJykKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGV4YzoKICAgICAgICAgICAgcHJpbnQoIiA+PiBGaWxlIG5vdCBmb3VuZCBcbiIpCiAgICBlbGlmIGNoPT0iMiI6CiAgICAgICAgcGljPWlucHV0KCdcbiA+PiBFbnRlciBSb2xsIE51bWJlciA6JykudXBwZXIoKQogICAgICAgIGlmIHBpYz09IjIwMDNBNTMwMTUiOgogICAgICAgICAgICBwcmludCgiXG4gPj4gTm90IGFsbG93ZWQgdG8gZG93bmxvYWQgNEs1SDRZIDRSSlVOJ3MgaW1hZ2VzIG9fTy4gQmV0d2VlbiBuaWNlIHRyeSEiKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHN0cjEgPSBteUVuY3J5cHRlZE1lc3NhZ2UxCiAgICAgICAgICAgIHByaW50KCdcbiA+PiB'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
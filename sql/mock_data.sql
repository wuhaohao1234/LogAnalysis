INSERT INTO `log_analysis`.`site_info`
    (`title`, `site_copyright`) value
    ('log_analysis', '吉数智安');

INSERT INTO `log_analysis`.`user`
    (`username`, `password`, `enable`, `role`) value ('system', '', 0, '管理员');
INSERT INTO `log_analysis`.`user`
    (`username`, `password`, `role`)
values ('admin',
        'pbkdf2:sha256:600000$564FLfbST0LQ6ast$ee84dc5b3544219a84dbee4872ba8be876cb4cbd3bb898ebd8ddd54d523289a6',
        '管理员')
     , ('wang',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('zhang',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('gao', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('hu', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('he', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('liu', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('li', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('zhao',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('wu', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('yang',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('guan',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('feng',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('fang',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('xiu', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('ma', 'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员')
     , ('huang',
        'pbkdf2:sha256:600000$AvOeGPzu1C52ICI0$e680be312ded61b12adb019a79a8ef558bba096211f525c7819a11fe5e3614a3',
        '普通会员');


INSERT INTO `log_analysis`.`scan_user_roles`
    (user_id, role_id)
values (1, 1),
       (2, 1),
       (3, 2);


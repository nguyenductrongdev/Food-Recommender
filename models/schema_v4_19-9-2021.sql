/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     9/19/2021 1:34:55 PM                         */
/*==============================================================*/


drop table if exists DANH_MUC_DON_VI_TINH;

drop table if exists DANH_MUC_THUC_PHAM;

drop table if exists NGUOI_DUNG;

drop table if exists NHU_CAU_MUA;

drop table if exists NHU_CAU_MUA_DANH_MUC_THUC_PHAM;

drop table if exists THUC_PHAM;

/*==============================================================*/
/* Table: DANH_MUC_DON_VI_TINH                                  */
/*==============================================================*/
create table DANH_MUC_DON_VI_TINH
(
   DMDVT_MA             int not null auto_increment,
   DMDVT_TEN            varchar(50),
   primary key (DMDVT_MA)
);

/*==============================================================*/
/* Table: DANH_MUC_THUC_PHAM                                    */
/*==============================================================*/
create table DANH_MUC_THUC_PHAM
(
   DMTP_MA              int not null auto_increment,
   DMTP_TEN             varchar(100),
   DMTP_MA_DMTM_CHA     int,
   primary key (DMTP_MA)
);

/*==============================================================*/
/* Table: NGUOI_DUNG                                            */
/*==============================================================*/
create table NGUOI_DUNG
(
   ND_MA                int not null auto_increment,
   ND_HO_TEN            varchar(100),
   ND_DIA_CHI           varchar(255),
   ND_SO_DIEN_THOAI     varchar(10),
   ND_EMAIL             varchar(255),
   ND_MAT_KHAU          varchar(50),
   ND_TAI_KHOAN         varchar(50),
   primary key (ND_MA)
);

/*==============================================================*/
/* Table: NHU_CAU_MUA                                           */
/*==============================================================*/
create table NHU_CAU_MUA
(
   NCM_MA               int not null auto_increment,
   ND_MA                int not null,
   DMDVT_MA             int not null,
   NCM_SO_LUONG         int,
   NCM_THOI_GIAN        varchar(10),
   primary key (NCM_MA)
);

/*==============================================================*/
/* Table: NHU_CAU_MUA_DANH_MUC_THUC_PHAM                        */
/*==============================================================*/
create table NHU_CAU_MUA_DANH_MUC_THUC_PHAM
(
   NCM_MA               int not null,
   DMTP_MA              int not null,
   primary key (NCM_MA, DMTP_MA)
);

/*==============================================================*/
/* Table: THUC_PHAM                                             */
/*==============================================================*/
create table THUC_PHAM
(
   TP_MA                int not null auto_increment,
   DMTP_MA              int not null,
   ND_MA                int not null,
   DMDVT_MA             int not null,
   TP_MO_TA             varchar(500),
   TP_HINH_ANH          varchar(255),
   TP_DON_GIA           int,
   TP_SO_LUONG          int,
   TP_NGAY_BAN          varchar(10),
   TP_VI_TRI_BAN_DO     varchar(50),
   primary key (TP_MA)
);

alter table NHU_CAU_MUA add constraint FK_NCM_DMDVT foreign key (DMDVT_MA)
      references DANH_MUC_DON_VI_TINH (DMDVT_MA) on delete restrict on update restrict;

alter table NHU_CAU_MUA add constraint FK_ND_NCM foreign key (ND_MA)
      references NGUOI_DUNG (ND_MA) on delete restrict on update restrict;

alter table NHU_CAU_MUA_DANH_MUC_THUC_PHAM add constraint FK_NHU_CAU_MUA_DANH_MUC_THUC_PHAM foreign key (NCM_MA)
      references NHU_CAU_MUA (NCM_MA) on delete restrict on update restrict;

alter table NHU_CAU_MUA_DANH_MUC_THUC_PHAM add constraint FK_NHU_CAU_MUA_DANH_MUC_THUC_PHAM2 foreign key (DMTP_MA)
      references DANH_MUC_THUC_PHAM (DMTP_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_BAN foreign key (ND_MA)
      references NGUOI_DUNG (ND_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_DMTP_TP foreign key (DMTP_MA)
      references DANH_MUC_THUC_PHAM (DMTP_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_TP_DVT foreign key (DMDVT_MA)
      references DANH_MUC_DON_VI_TINH (DMDVT_MA) on delete restrict on update restrict;


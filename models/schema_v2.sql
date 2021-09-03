/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     9/2/2021 5:00:26 PM                          */
/*==============================================================*/


drop table if exists LOAI_THUC_PHAM;

drop table if exists LTP_NCM;

drop table if exists NGUOI_DUNG;

drop table if exists NHU_CAU_MUA;

drop table if exists THUC_PHAM;

/*==============================================================*/
/* Table: LOAI_THUC_PHAM                                        */
/*==============================================================*/
create table LOAI_THUC_PHAM
(
   LTP_MA               int not null auto_increment,
   LTP_TEN              varchar(255),
   primary key (LTP_MA)
);

/*==============================================================*/
/* Table: LTP_NCM                                               */
/*==============================================================*/
create table LTP_NCM
(
   LTP_MA               int not null,
   NCM_MA               int not null,
   primary key (LTP_MA, NCM_MA)
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
   ND_VI_TRI            varchar(50),
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
   NCM_SO_LUONG         int,
   NCM_DON_VI           varchar(50),
   primary key (NCM_MA)
);

/*==============================================================*/
/* Table: THUC_PHAM                                             */
/*==============================================================*/
create table THUC_PHAM
(
   TP_MA                int not null auto_increment,
   ND_MA                int not null,
   LTP_MA               int not null,
   TP_MO_TA             varchar(500),
   TP_HINH_ANH          varchar(255),
   TP_DON_GIA           int,
   TP_SO_LUONG          int,
   TP_DON_VI            varchar(50),
   primary key (TP_MA)
);

alter table LTP_NCM add constraint FK_LTP_NCM foreign key (LTP_MA)
      references LOAI_THUC_PHAM (LTP_MA) on delete restrict on update restrict;

alter table LTP_NCM add constraint FK_LTP_NCM2 foreign key (NCM_MA)
      references NHU_CAU_MUA (NCM_MA) on delete restrict on update restrict;

alter table NHU_CAU_MUA add constraint FK_ND_NCM foreign key (ND_MA)
      references NGUOI_DUNG (ND_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_BAN foreign key (ND_MA)
      references NGUOI_DUNG (ND_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_TP_LTP foreign key (LTP_MA)
      references LOAI_THUC_PHAM (LTP_MA) on delete restrict on update restrict;


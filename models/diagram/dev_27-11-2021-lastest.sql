/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     11/27/2021 11:17:22 AM                       */
/*==============================================================*/


drop table if exists BINH_LUAN;

drop table if exists CHI_TIET_DANG_KY_MUA;

drop table if exists DANG_KY_MUA;

drop table if exists DANH_MUC_DON_VI_TINH;

drop table if exists DANH_MUC_THUC_PHAM;

drop table if exists DM_DON_VI_TINH_DM_THUC_PHAM;

drop table if exists NGUOI_DUNG;

drop table if exists THUC_PHAM;

/*==============================================================*/
/* Table: BINH_LUAN                                             */
/*==============================================================*/
create table BINH_LUAN
(
   BL_MA                int not null auto_increment,
   ND_MA                int not null,
   TP_MA                int not null,
   BL_THOI_GIAN         varchar(10),
   BL_NOI_DUNG          varchar(500),
   primary key (BL_MA)
);

/*==============================================================*/
/* Table: CHI_TIET_DANG_KY_MUA                                  */
/*==============================================================*/
create table CHI_TIET_DANG_KY_MUA
(
   TP_MA                int not null,
   DKM_MA               int not null,
   CTDKM_SO_LUONG       float,
   CTDKM_GHI_CHU        varchar(255),
   CTDKM_TRANG_THAI     int,
   primary key (TP_MA, DKM_MA)
);

/*==============================================================*/
/* Table: DANG_KY_MUA                                           */
/*==============================================================*/
create table DANG_KY_MUA
(
   DKM_MA               int not null auto_increment,
   ND_MA                int,
   DKM_THOI_GIAN        varchar(10),
   DKM_VI_TRI_BAN_DO    varchar(50),
   DKM_DIA_CHI          varchar(255),
   primary key (DKM_MA)
);

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
/* Table: DM_DON_VI_TINH_DM_THUC_PHAM                           */
/*==============================================================*/
create table DM_DON_VI_TINH_DM_THUC_PHAM
(
   DMTP_MA              int not null,
   DMDVT_MA             int not null,
   primary key (DMTP_MA, DMDVT_MA)
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
/* Table: THUC_PHAM                                             */
/*==============================================================*/
create table THUC_PHAM
(
   TP_MA                int not null auto_increment,
   DMDVT_MA             int not null,
   ND_MA                int not null,
   DMTP_MA              int not null,
   TP_TEN               varchar(50),
   TP_MO_TA             varchar(500),
   TP_HINH_ANH          varchar(255),
   TP_DON_GIA           int,
   TP_SO_LUONG          float,
   TP_NGAY_BAN          varchar(10),
   TP_VI_TRI_BAN_DO     varchar(50),
   TP_DIA_CHI           varchar(255),
   TP_SUAT_BAN          float,
   primary key (TP_MA)
);

alter table BINH_LUAN add constraint FK_BL_TP foreign key (TP_MA)
      references THUC_PHAM (TP_MA) on delete restrict on update restrict;

alter table BINH_LUAN add constraint FK_ND_BL foreign key (ND_MA)
      references NGUOI_DUNG (ND_MA) on delete restrict on update restrict;

alter table CHI_TIET_DANG_KY_MUA add constraint FK_CTDKM_DKM foreign key (DKM_MA)
      references DANG_KY_MUA (DKM_MA) on delete restrict on update restrict;

alter table CHI_TIET_DANG_KY_MUA add constraint FK_CTKDM_TP foreign key (TP_MA)
      references THUC_PHAM (TP_MA) on delete restrict on update restrict;

alter table DANG_KY_MUA add constraint FK_ND_DKM foreign key (ND_MA)
      references NGUOI_DUNG (ND_MA) on delete restrict on update restrict;

alter table DM_DON_VI_TINH_DM_THUC_PHAM add constraint FK_DM_DON_VI_TINH_DM_THUC_PHAM foreign key (DMTP_MA)
      references DANH_MUC_THUC_PHAM (DMTP_MA) on delete restrict on update restrict;

alter table DM_DON_VI_TINH_DM_THUC_PHAM add constraint FK_DM_DON_VI_TINH_DM_THUC_PHAM2 foreign key (DMDVT_MA)
      references DANH_MUC_DON_VI_TINH (DMDVT_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_BAN foreign key (ND_MA)
      references NGUOI_DUNG (ND_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_DMDVT_TP foreign key (DMDVT_MA)
      references DANH_MUC_DON_VI_TINH (DMDVT_MA) on delete restrict on update restrict;

alter table THUC_PHAM add constraint FK_DMTP_TP foreign key (DMTP_MA)
      references DANH_MUC_THUC_PHAM (DMTP_MA) on delete restrict on update restrict;


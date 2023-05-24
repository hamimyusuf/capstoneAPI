/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     13/05/2023 10.51.39                          */
/*==============================================================*/


drop table if exists HISTORY;

drop table if exists INPUT;

drop table if exists RESULT;

drop table if exists USER;

/*==============================================================*/
/* Table: HISTORY                                               */
/*==============================================================*/
create table HISTORY
(
   ID_HISTORY           varchar(64) not null,
   USERNAME             varchar(100),
   ID_INPUT             varchar(64),
   ID_RESULT            varchar(64),
   DATE                 date not null,
   primary key (ID_HISTORY)
);

/*==============================================================*/
/* Table: INPUT                                                 */
/*==============================================================*/
create table INPUT
(
   ID_INPUT             varchar(64) not null,
   ID_HISTORY           varchar(64),
   FILENAME             varchar(100) not null,
   primary key (ID_INPUT)
);

/*==============================================================*/
/* Table: RESULT                                                */
/*==============================================================*/
create table RESULT
(
   ID_RESULT            varchar(64) not null,
   ID_HISTORY           varchar(64),
   DESCRIPTION          text not null,
   SOLUTION             text not null,
   primary key (ID_RESULT)
);

/*==============================================================*/
/* Table: USER                                                  */
/*==============================================================*/
create table USER
(
   USERNAME             varchar(100) not null,
   NAME                 varchar(128) not null,
   PASSWORD             varchar(256) not null,
   primary key (USERNAME)
);

alter table HISTORY add constraint FK_RELATIONSHIP_1 foreign key (USERNAME)
      references USER (USERNAME) on delete restrict on update restrict;

alter table HISTORY add constraint FK_RELATIONSHIP_4 foreign key (ID_INPUT)
      references INPUT (ID_INPUT) on delete restrict on update restrict;

alter table HISTORY add constraint FK_RELATIONSHIP_5 foreign key (ID_RESULT)
      references RESULT (ID_RESULT) on delete restrict on update restrict;

alter table INPUT add constraint FK_RELATIONSHIP_2 foreign key (ID_HISTORY)
      references HISTORY (ID_HISTORY) on delete restrict on update restrict;

alter table RESULT add constraint FK_RELATIONSHIP_3 foreign key (ID_HISTORY)
      references HISTORY (ID_HISTORY) on delete restrict on update restrict;


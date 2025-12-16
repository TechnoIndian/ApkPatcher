.class public Lorg/telegram/abhi/Hook;
.super Ljava/lang/Object;
.source "SourceFile"


# static fields
.field public static candelMessages:Z


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static hook()V
    .registers 1

    const/4 v0, 0x1

    .line 17
    invoke-static {v0}, Lorg/telegram/abhi/Hook;->setCanDelMessages(Z)V

    return-void
.end method

.method public static setCanDelMessages(Z)V
    .registers 4

    sput-boolean p0, Lorg/telegram/abhi/Hook;->candelMessages:Z

    sget-object v0, Lorg/telegram/messenger/ApplicationLoader;->applicationContext:Landroid/content/Context;

    const-string v1, "mainconfig"

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v0

    invoke-interface {v0}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;

    move-result-object v0

    const-string v1, "candelMessages"

    invoke-interface {v0, v1, p0}, Landroid/content/SharedPreferences$Editor;->putBoolean(Ljava/lang/String;Z)Landroid/content/SharedPreferences$Editor;

    move-result-object v0

    invoke-interface {v0}, Landroid/content/SharedPreferences$Editor;->apply()V

    return-void
.end method

.method public static unhook()V
    .registers 1

    .line 23
    sget-boolean v0, Lorg/telegram/abhi/Hook;->candelMessages:Z

    if-eqz v0, :cond_8

    const/4 v0, 0x0

    .line 24
    invoke-static {v0}, Lorg/telegram/abhi/Hook;->setCanDelMessages(Z)V

    :cond_8
    return-void
.end method
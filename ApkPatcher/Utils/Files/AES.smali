.class public LRK_TECHNO_INDIA/AES;
.super Ljava/lang/Thread;
# static fields
.field private static final PARAMETER_BUFFER:Ljava/lang/ThreadLocal;
.field private static final QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
.field private static final TIME_FORMAT1:Ljava/text/SimpleDateFormat;
.field private static final TIME_FORMAT2:Ljava/text/SimpleDateFormat;
# direct methods
.method static constructor <clinit>()V
    .registers 2
    new-instance v0, Ljava/text/SimpleDateFormat;
    const-string v1, "HH:mm:ss.SSS"
    invoke-direct {v0, v1}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;)V
    sput-object v0, LRK_TECHNO_INDIA/AES;->TIME_FORMAT1:Ljava/text/SimpleDateFormat;
    new-instance v0, Ljava/text/SimpleDateFormat;
    const-string v1, "yyyyMMddHHmmssSSS"
    invoke-direct {v0, v1}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;)V
    sput-object v0, LRK_TECHNO_INDIA/AES;->TIME_FORMAT2:Ljava/text/SimpleDateFormat;
    new-instance v0, Ljava/util/concurrent/LinkedBlockingQueue;
    invoke-direct {v0}, Ljava/util/concurrent/LinkedBlockingQueue;-><init>()V
    sput-object v0, LRK_TECHNO_INDIA/AES;->QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
    new-instance v0, Ljava/lang/ThreadLocal;
    invoke-direct {v0}, Ljava/lang/ThreadLocal;-><init>()V
    sput-object v0, LRK_TECHNO_INDIA/AES;->PARAMETER_BUFFER:Ljava/lang/ThreadLocal;
    new-instance v0, LRK_TECHNO_INDIA/AES;
    invoke-direct {v0}, LRK_TECHNO_INDIA/AES;-><init>()V
    const/4 v1, 0x1
    invoke-virtual {v0, v1}, LRK_TECHNO_INDIA/AES;->setDaemon(Z)V
    invoke-virtual {v0}, LRK_TECHNO_INDIA/AES;->start()V
    return-void
.end method
.method public constructor <init>()V
    .registers 1
    invoke-direct {p0}, Ljava/lang/Thread;-><init>()V
    return-void
.end method
.method public static a(Ljava/lang/Object;)V
    .registers 2
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->z(Ljava/lang/String;)V
    return-void
.end method
.method public static b()V
    .registers 2
    sget-object v0, LRK_TECHNO_INDIA/AES;->PARAMETER_BUFFER:Ljava/lang/ThreadLocal;
    invoke-virtual {v0}, Ljava/lang/ThreadLocal;->get()Ljava/lang/Object;
    move-result-object v1
    check-cast v1, Ljava/lang/StringBuilder;
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v1
    invoke-static {v1}, LRK_TECHNO_INDIA/AES;->z(Ljava/lang/String;)V
    invoke-virtual {v0}, Ljava/lang/ThreadLocal;->remove()V
    return-void
.end method
.method public static b1(Ljava/lang/Object;)V
    .registers 3
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    const-string v1, "𝐃𝐚𝐭𝐚 ︻デ═一 "
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->x(Ljava/lang/String;)V
    return-void
.end method
.method public static b2(Ljava/lang/Object;)V
    .registers 3
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    const-string v1, "𝐃𝐚𝐭𝐚/𝐊𝐞𝐲 ︻デ═一 "
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->x(Ljava/lang/String;)V
    return-void
.end method
.method public static b3(Ljava/lang/Object;)V
    .registers 3
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    const-string v1, "𝐈𝐕/𝐊𝐞𝐲 ︻デ═一 "
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->x(Ljava/lang/String;)V
    return-void
.end method
.method public static b4(Ljava/lang/Object;)V
    .registers 3
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    const-string v1, "𝐏𝐚𝐫𝐚𝐦𝐞𝐭𝐞𝐫 4 ︻デ═一 "
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->x(Ljava/lang/String;)V
    return-void
.end method
.method public static b5(Ljava/lang/Object;)V
    .registers 3
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    const-string v1, "𝐏𝐚𝐫𝐚𝐦𝐞𝐭𝐞𝐫 5 ︻デ═一 "
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->x(Ljava/lang/String;)V
    return-void
.end method
.method public static b6(Ljava/lang/Object;)V
    .registers 3
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    const-string v1, "𝐏𝐚𝐫𝐚𝐦𝐞𝐭𝐞𝐫 6 ︻デ═一 "
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->x(Ljava/lang/String;)V
    return-void
.end method
.method public static getInstance(Ljava/lang/Object;)V
    .registers 3
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V
    const-string v1, "\ud835\ude3e\ud835\ude5e\ud835\ude65\ud835\ude5d\ud835\ude5a\ud835\ude67 \ud835\ude3c\ud835\ude61\ud835\ude5c\ud835\ude64\ud835\ude67\ud835\ude5e\ud835\ude69\ud835\ude5d\ud835\ude62 ︻デ═一 "
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-static {p0}, LRK_TECHNO_INDIA/AES;->y(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, LRK_TECHNO_INDIA/AES;->x(Ljava/lang/String;)V
    return-void
.end method
.method private static x(Ljava/lang/String;)V
    .registers 4
    sget-object v0, LRK_TECHNO_INDIA/AES;->PARAMETER_BUFFER:Ljava/lang/ThreadLocal;
    invoke-virtual {v0}, Ljava/lang/ThreadLocal;->get()Ljava/lang/Object;
    move-result-object v1
    check-cast v1, Ljava/lang/StringBuilder;
    if-nez v1, :cond_13
    new-instance v2, Ljava/lang/StringBuilder;
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V
    move-object v1, v2
    invoke-virtual {v0, v1}, Ljava/lang/ThreadLocal;->set(Ljava/lang/Object;)V
    :cond_13
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->length()I
    move-result v0
    if-lez v0, :cond_1e
    const/16 v0, 0xa
    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;
    :cond_1e
    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    return-void
.end method

.method private static y(Ljava/lang/Object;)Ljava/lang/String;
    .registers 3
    if-nez p0, :cond_5
    const-string v0, "null"
    return-object v0
    :cond_5
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;
    move-result-object v0
    invoke-virtual {v0}, Ljava/lang/Class;->isArray()Z
    move-result v1
    if-eqz v1, :cond_77
    const-class v1, [B
    if-ne v0, v1, :cond_1b
    move-object v1, p0
    check-cast v1, [B
    invoke-static {v1}, Ljava/util/Arrays;->toString([B)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_1b
    const-class v1, [S
    if-ne v0, v1, :cond_27
    move-object v1, p0
    check-cast v1, [S
    invoke-static {v1}, Ljava/util/Arrays;->toString([S)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_27
    const-class v1, [I
    if-ne v0, v1, :cond_33
    move-object v1, p0
    check-cast v1, [I
    invoke-static {v1}, Ljava/util/Arrays;->toString([I)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_33
    const-class v1, [J
    if-ne v0, v1, :cond_3f
    move-object v1, p0
    check-cast v1, [J
    invoke-static {v1}, Ljava/util/Arrays;->toString([J)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_3f
    const-class v1, [C
    if-ne v0, v1, :cond_4b
    move-object v1, p0
    check-cast v1, [C
    invoke-static {v1}, Ljava/util/Arrays;->toString([C)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_4b
    const-class v1, [F
    if-ne v0, v1, :cond_57
    move-object v1, p0
    check-cast v1, [F
    invoke-static {v1}, Ljava/util/Arrays;->toString([F)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_57
    const-class v1, [D
    if-ne v0, v1, :cond_63
    move-object v1, p0
    check-cast v1, [D
    invoke-static {v1}, Ljava/util/Arrays;->toString([D)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_63
    const-class v1, [Z
    if-ne v0, v1, :cond_6f
    move-object v1, p0
    check-cast v1, [Z
    invoke-static {v1}, Ljava/util/Arrays;->toString([Z)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_6f
    move-object v1, p0
    check-cast v1, [Ljava/lang/Object;
    invoke-static {v1}, Ljava/util/Arrays;->deepToString([Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :cond_77
    invoke-virtual {p0}, Ljava/lang/Object;->toString()Ljava/lang/String;
    move-result-object v1
    return-object v1
.end method
.method private static z(Ljava/lang/String;)V
    .registers 8
    const-string v0, "================== \ud83c\uddee\ud83c\uddf3 \ud835\ude3f\ud835\ude5a\ud835\ude58\ud835\ude67\ud835\ude6e\ud835\ude65\ud835\ude69\ud835\ude5a\ud835\ude59 \ud835\ude3d\ud835\ude6e \ud835\ude4f\ud835\ude5a\ud835\ude58\ud835\ude5d\ud835\ude63\ud835\ude64 \ud835\ude44\ud835\ude63\ud835\ude59\ud835\ude5e\ud835\ude56 \ud83c\uddee\ud83c\uddf3 ==================\n\n[RESULT]\n\n"
    const-string v1, "[TIME]"
    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z
    move-result v2
    if-eqz v2, :cond_1c
    sget-object v2, LRK_TECHNO_INDIA/AES;->TIME_FORMAT1:Ljava/text/SimpleDateFormat;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v3
    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v3
    invoke-virtual {v2, v3}, Ljava/text/SimpleDateFormat;->format(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    :cond_1c
    new-instance v1, Ljava/lang/Throwable;
    invoke-direct {v1}, Ljava/lang/Throwable;-><init>()V
    invoke-virtual {v1}, Ljava/lang/Throwable;->getStackTrace()[Ljava/lang/StackTraceElement;
    move-result-object v1
    const/4 v2, 0x2
    aget-object v1, v1, v2
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getFileName()Ljava/lang/String;
    move-result-object v2
    if-nez v2, :cond_30
    const-string v2, "Unknown Source"
    :cond_30
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getLineNumber()I
    move-result v3
    if-ltz v3, :cond_4a
    new-instance v4, Ljava/lang/StringBuilder;
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V
    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v5, ":"
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v2
    :cond_4a
    const-string v4, "[RESULT]"
    invoke-virtual {v0, v4, p0}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v4
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getClassName()Ljava/lang/String;
    move-result-object v5
    const-string v6, "[CLASS]"
    invoke-virtual {v4, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v4
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getMethodName()Ljava/lang/String;
    move-result-object v5
    const-string v6, "[METHOD]"
    invoke-virtual {v4, v6, v5}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v4
    const-string v5, "[LOCATION]"
    invoke-virtual {v4, v5, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v0
    sget-object v4, LRK_TECHNO_INDIA/AES;->QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
    invoke-virtual {v4, v0}, Ljava/util/concurrent/LinkedBlockingQueue;->offer(Ljava/lang/Object;)Z
    return-void
.end method
# virtual methods
.method public run()V
    .registers 10
    const/4 v0, 0x0
    const-string v1, "[SDCARD]/MT2/logs/[PACKAGE]-[TIME].json"
    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;
    move-result-object v2
    invoke-virtual {v2}, Ljava/io/File;->getPath()Ljava/lang/String;
    move-result-object v2
    const-string v3, "[SDCARD]"
    invoke-virtual {v1, v3, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    const-string v2, "[PACKAGE]"
    const-string v3, "PACKAGENAME"
    invoke-virtual {v1, v2, v3}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    sget-object v2, LRK_TECHNO_INDIA/AES;->TIME_FORMAT2:Ljava/text/SimpleDateFormat;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v3
    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v3
    invoke-virtual {v2, v3}, Ljava/text/SimpleDateFormat;->format(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v2
    const-string v3, "[TIME]"
    invoke-virtual {v1, v3, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    const/16 v2, 0x5c
    const/16 v3, 0x2f
    invoke-virtual {v1, v2, v3}, Ljava/lang/String;->replace(CC)Ljava/lang/String;
    move-result-object v2
    const-string v3, "//"
    const-string v4, "/"
    invoke-virtual {v2, v3, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
    move-result-object v1
    const/4 v2, 0x0
    :try_start_3e
    new-instance v3, Ljava/io/File;
    invoke-direct {v3, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V
    invoke-virtual {v3}, Ljava/io/File;->getParentFile()Ljava/io/File;
    move-result-object v4
    if-eqz v4, :cond_4c
    invoke-virtual {v4}, Ljava/io/File;->mkdirs()Z
    :cond_4c
    new-instance v5, Ljava/io/FileOutputStream;
    const/4 v6, 0x1
    invoke-direct {v5, v3, v6}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;Z)V
    :try_end_52
    .catch Ljava/io/IOException; {:try_start_3e .. :try_end_52} :catch_54
    move-object v0, v5
    goto :goto_59
    :catch_54
    move-exception v3
    invoke-virtual {v3}, Ljava/io/IOException;->printStackTrace()V
    move-object v2, v3
    :goto_59
    if-nez v0, :cond_9a
    :try_start_5b
    new-instance v3, Ljava/io/File;
    const-string v4, "/data/data/PACKAGENAME/logs"
    invoke-direct {v3, v4}, Ljava/io/File;-><init>(Ljava/lang/String;)V
    new-instance v4, Ljava/io/File;
    new-instance v5, Ljava/lang/StringBuilder;
    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V
    sget-object v6, LRK_TECHNO_INDIA/AES;->TIME_FORMAT2:Ljava/text/SimpleDateFormat;
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v7
    invoke-static {v7, v8}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v7
    invoke-virtual {v6, v7}, Ljava/text/SimpleDateFormat;->format(Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v6
    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v6, ".log"
    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v5
    invoke-direct {v4, v3, v5}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V
    invoke-virtual {v3}, Ljava/io/File;->mkdirs()Z
    new-instance v5, Ljava/io/FileOutputStream;
    invoke-direct {v5, v4}, Ljava/io/FileOutputStream;-><init>(Ljava/io/File;)V
    :try_end_8e
    .catch Ljava/io/IOException; {:try_start_5b .. :try_end_8e} :catch_90
    move-object v0, v5
    goto :goto_9a
    :catch_90
    move-exception v3
    invoke-virtual {v3}, Ljava/io/IOException;->printStackTrace()V
    new-instance v4, Ljava/lang/RuntimeException;
    invoke-direct {v4, v2}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/Throwable;)V
    throw v4
    :cond_9a
    :goto_9a
    :try_start_9a
    invoke-static {}, Ljava/nio/charset/Charset;->defaultCharset()Ljava/nio/charset/Charset;
    move-result-object v3
    :goto_9e
    sget-object v4, LRK_TECHNO_INDIA/AES;->QUEUE:Ljava/util/concurrent/LinkedBlockingQueue;
    invoke-virtual {v4}, Ljava/util/concurrent/LinkedBlockingQueue;->take()Ljava/lang/Object;
    move-result-object v5
    check-cast v5, Ljava/lang/String;
    invoke-virtual {v5, v3}, Ljava/lang/String;->getBytes(Ljava/nio/charset/Charset;)[B
    move-result-object v6
    invoke-virtual {v0, v6}, Ljava/io/FileOutputStream;->write([B)V
    invoke-virtual {v4}, Ljava/util/concurrent/LinkedBlockingQueue;->isEmpty()Z
    move-result v4
    if-eqz v4, :cond_b6
    invoke-virtual {v0}, Ljava/io/FileOutputStream;->flush()V
    :try_end_b6
    .catch Ljava/lang/Exception; {:try_start_9a .. :try_end_b6} :catch_b7
    :cond_b6
    goto :goto_9e
    :catch_b7
    move-exception v3
    new-instance v4, Ljava/lang/RuntimeException;
    invoke-direct {v4, v3}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/Throwable;)V
    throw v4
.end method

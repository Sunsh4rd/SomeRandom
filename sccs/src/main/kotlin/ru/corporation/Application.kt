package ru.corporation

import io.ktor.server.application.*
import ru.corporation.plugins.configureDatabases
import ru.corporation.plugins.configureRouting
import ru.corporation.plugins.configureSerialization

fun main(args: Array<String>): Unit = io.ktor.server.netty.EngineMain.main(args)

fun Application.module() {
    configureSerialization()
    configureDatabases()
    configureRouting()
}

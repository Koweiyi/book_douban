package com.iedu.demo.doubandemo;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;

@SpringBootApplication
@Configuration
@MapperScan("com.iedu.demo.doubandemo.dao")
public class DoubandemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DoubandemoApplication.class, args);
    }

}

package com.hoangvinh.bai2.controllers;

import com.hoangvinh.bai2.dto.UserCreateRequest;
import com.hoangvinh.bai2.dto.UserResponse;
import com.hoangvinh.bai2.services.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1")
public class UserController {

    private final UserService userService;

    @GetMapping("/users")
    public ResponseEntity<List<UserResponse>> getAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }

    @GetMapping("/users/{id}")
    public ResponseEntity<UserResponse> findById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.findUserById(id));
    }


    @PostMapping("/users")
    public ResponseEntity<UserResponse> createUser(@RequestBody UserCreateRequest userCreateRequest) {
        return ResponseEntity.status(HttpStatus.CREATED).body(userService.createUser(userCreateRequest));
    }
}

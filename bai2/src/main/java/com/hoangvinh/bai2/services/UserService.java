package com.hoangvinh.bai2.services;

import com.hoangvinh.bai2.dto.UserCreateRequest;
import com.hoangvinh.bai2.dto.UserResponse;
import com.hoangvinh.bai2.mappers.UserMapper;
import com.hoangvinh.bai2.model.User;
import com.hoangvinh.bai2.repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final UserMapper userMapper;

    public UserResponse createUser(UserCreateRequest userCreateRequest) {
        User user = User.builder()
                .email(userCreateRequest.getEmail())
                .username(userCreateRequest.getUsername())
                .build();
        return userMapper.toResponse(userRepository.save(user));
    }
}
